import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 


pickle_in = open("Linear_Housing_model.pkl","rb")
regression=pickle.load(pickle_in)


def main():
    st.title("House Price Prediction")
    MedInc = st.text_input("MedInc","")
    HouseAge = st.text_input("HouseAge","")
    AveRooms = st.text_input("AveRooms","")
    AveBedrms = st.text_input("AveBedrms","")
    Population = st.text_input("Population","")
    AveOccup = st.text_input("AveOccup","")
    Latitude = st.text_input("Latitude","")
    Longitude = st.text_input("Longitude","")
    result=""
    if st.button("Predict"):
        result=regression.predict([[eval(MedInc), eval(HouseAge), eval(AveRooms), 
                                           eval(AveBedrms),eval(Population), eval(AveOccup), 
                                           eval(Latitude), eval(Longitude)]])
    st.success('The output is {}'.format(result))
    st.write(result)

if __name__=='__main__':
    main()