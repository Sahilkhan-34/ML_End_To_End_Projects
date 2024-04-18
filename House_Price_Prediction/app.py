import numpy as np
import pickle
import pandas as pd
from flask import Flask, request


app= Flask(__name__)

pickel_in = open("Linear_Housing_model.pkl", "rb")
regression = pickle.load(pickel_in)

@app.route('/')      # decorator
def welcome():
    return "Welcome All"

@app.route('/predict', methods=["GET"])
def predict_note_authentication():
    input_cols = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms',
     'Population', 'AveOccup', 'Latitude', 'Longitude']
    
    list1 = []
    for i in input_cols:
        val=request.args.get(i)
        list1.append(eval(val))

    prediction = regression.predict([list1])

    print(prediction)
    return 'House Price Prediction is' +str(prediction)

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)