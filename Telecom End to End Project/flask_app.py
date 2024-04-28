import numpy as np
import joblib
import pandas as pd
from flask import Flask, request
 

app=Flask(__name__)
joblib_in = open("best_Random_forest_model.joblib","rb")
model=joblib.load(joblib_in)


@app.route('/')      # decorator
def welcome():
    return "Welcome All"


@app.route('/predict',methods=["GET"])
def predict_note_authentication():

    """
    ['gender','age','no_of_days_subscribed','multi_screen',	'mail_subscribed','weekly_mins_watched','minimum_daily_mins',
    'maximum_daily_mins','weekly_max_night_mins','videos_watched','maximum_days_inactive','customer_support_calls']

    ['gender', 'age', 'no_of_days_subscribed', 'multi_screen',
       'mail_subscribed', 'weekly_mins_watched', 'minimum_daily_mins',
       'maximum_daily_mins', 'weekly_max_night_mins', 'videos_watched',
       'maximum_days_inactive', 'customer_support_calls']
   """
    input_cols=['gender', 'age', 'no_of_days_subscribed', 'multi_screen',
       'mail_subscribed', 'weekly_mins_watched', 'minimum_daily_mins',
       'maximum_daily_mins', 'weekly_max_night_mins', 'videos_watched',
       'maximum_days_inactive', 'customer_support_calls']
    list1=[]
    for i in input_cols:
        val=request.args.get(i)
        list1.append(eval(val))


    prediction=model.predict([list1])

    #prediction=model.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return "Hello The answer is"+str(prediction)




if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)