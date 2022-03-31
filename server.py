import flask
import os
from tensorflow import keras
import numpy as np


from flask_restplus import Api
from documented_endpoints import namespace as hello_world_ns

blueprint = flask.Blueprint('documented_api', __name__, url_prefix='/documented_api')

api_extension = Api(
    blueprint,
    title='Flask RESTplus Demo',
    version='1.0',
    description='Application tutorial to demonstrate Flask RESTplus extension\
        for better project structure and auto generated documentation',
    doc='/doc'
)
api_extension.add_namespace(hello_world_ns)


model = keras.models.load_model('ecg_hearbeat_cnn_model')


app = flask.Flask(__name__)
app.config['RESTPLUS_MASK_SWAGGER'] = False
app.register_blueprint(blueprint)
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


@app.route('/predict', methods=['POST'])
def predict():
    features = flask.request.json['features']
    prediction = model.predict([features])
    print("prediction is", prediction)
    response = {'prediction': prediction_to_message(prediction[0])}
    return flask.jsonify(response)

# Categories
# 0) N means "Normal beat"

# 1) S means "Supraventricular premature beat"

# 2) V means "Premature ventricular contraction"

# 3) F means "Fusion of ventricular and normal beat"

# 4) Q means "Unclassifiable beat"

# https://towardsdatascience.com/accuracy-precision-recall-or-f1-331fb37c5cb9


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
