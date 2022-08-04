import numpy as np

from flask import Flask, jsonify, request, render_template
from flask_restful import Api, Resource, reqparse
import pickle
import numpy as np
import json

# load the model from disk
loaded_model = pickle.load(open('../models/titanic_model.pickle', 'rb'))

'''
int_features = [int(x) for x in request.form.values()]
final_features = [np.array(int_features)]
prediction = model.predict(final_features)
'''

input_data = (3, 0, 35, 0, 0)
input_data_as_numpy_array = np.asarray(input_data)
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
prediction = model.predict(input_data_reshaped)
print(prediction)

if prediction[0]==0 :
    print("Dead")
elif prediction[0]== 1:
    print("Alive")


app = Flask(__name__)
model = pickle.load(open('titanic_model.pkl', 'rb'))

def create_app(enviroment):
    app = Flask(__name__)
    return app

app = create_app()

app.route('/api/v1/users', methods=['GET'])
def get_users():
    response = {'message': 'success'}
    return jsonify(response)

app.route('/api/v1/users', methods=['GET'])
def get_users():
    response = {'message': 'success'}
    return jsonify(response)