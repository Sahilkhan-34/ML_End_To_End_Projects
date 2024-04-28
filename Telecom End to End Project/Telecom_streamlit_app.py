import numpy as np
import joblib
import pandas as pd
import streamlit as st 



joblib_in = open("best_Random_forest_model.joblib","rb")
model=joblib.load(joblib_in)


def main():
    st.title("Customer Churn Prediction")
    gender = st.text_input("gender","")
    age = st.text_input("age","")
    no_of_days_subscribed = st.text_input("no_of_days_subscribed","")
    multi_screen = st.text_input("multi_screen","")
    mail_subscribed = st.text_input("mail_subscribed","")
    weekly_mins_watched = st.text_input("weekly_mins_watched","")
    minimum_daily_mins = st.text_input("minimum_daily_mins","")
    maximum_daily_mins = st.text_input("maximum_daily_mins","")
    weekly_max_night_mins = st.text_input("weekly_max_night_mins","")
    videos_watched = st.text_input("videos_watched","")
    maximum_days_inactive = st.text_input("maximum_days_inactive","")
    customer_support_calls = st.text_input("customer_support_calls","")
    result=""
    if st.button("Predict"):
        result=model.predict([[eval(gender), eval(age), eval(no_of_days_subscribed), 
                                           eval(multi_screen),eval(mail_subscribed), eval(weekly_mins_watched), 
                                           eval(minimum_daily_mins), eval(maximum_daily_mins), eval(weekly_max_night_mins), eval(videos_watched), eval(maximum_days_inactive), eval(customer_support_calls),]])
    st.success('The output is {}'.format(result))
    st.write(result)

if __name__=='__main__':
    main()