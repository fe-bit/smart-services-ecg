from flask import request
from flask_restplus import Namespace, Resource, fields


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


namespace = Namespace('ecg_prediction', 'ECG Prediction related endpoints')

ecg_prediction_model = namespace.model('EcgPrediction', {
    'prediction': fields.String(
        readonly=True,
        description='ECG Prediction Message'
    )
})

ecg_prediciton_example = {'prediction': 'ECG Prediction'}
ecg_prediciton_0 = {'prediction': get_message_for_index(0)}
ecg_prediciton_1 = {'prediction': get_message_for_index(1)}
ecg_prediciton_2 = {'prediction': get_message_for_index(2)}
ecg_prediciton_3 = {'prediction': get_message_for_index(3)}
ecg_prediciton_4 = {'prediction': get_message_for_index(4)}



@namespace.route('')
class EcgPrediction(Resource):
    @namespace.doc('get_ecg_prediction')
    @namespace.marshal_list_with(ecg_prediction_model)
    @namespace.response(500, 'Internal Server error')    
    def post(self):
        '''ECG Prediction Endpoint'''

        return ecg_prediciton_example
