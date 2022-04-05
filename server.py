import flask
import os
from tensorflow import keras
import numpy as np


model = keras.models.load_model('ecg_hearbeat_cnn_model.h5')

app = flask.Flask(__name__)
port = int(os.getenv("PORT", 9099))


def get_message_for_index(index):
    if index == 0:
        return "Normal heartbeat"
    if index == 1:
        return "Supraventricular premature beat"
    if index == 2:
        return "Premature ventricular contraction"
    if index == 3:
        return "Fusion of ventricular and normal beat"
    if index == 4:
        return "Unclassifiable beat"


def prediction_to_message(prediction):
    index_max = np.argmax(prediction)
    value_max = prediction[index_max]
    if value_max > 0.95:
        return get_message_for_index(index_max)
    else:
        return "indefinite prediction"


def is_valid_ecg_data(ecg_data):
    def valid_length(data):
        return len(data) == 187

    def valid_entries(data):
        try:
            for entry in data:
                float(entry)
            return True
        except:
            return False

    return valid_length(ecg_data) and valid_entries(ecg_data)


@app.route('/predict', methods=['POST'])
def predict():
    features = flask.request.json['ecg_data']
    try:
        prediction = model.predict([features])
        print("prediction is", prediction)
        response = {'prediction': prediction_to_message(prediction[0])}
        return flask.jsonify(response)
    except:
        return flask.Response({'error': 'Invalid Input'}, status=400)

# Categories
# 0) N means "Normal beat"

# 1) S means "Supraventricular premature beat"

# 2) V means "Premature ventricular contraction"

# 3) F means "Fusion of ventricular and normal beat"

# 4) Q means "Unclassifiable beat"

# https://towardsdatascience.com/accuracy-precision-recall-or-f1-331fb37c5cb9


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
    