import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler

model = joblib.load('model.h5')
scaler = joblib.load('scaler.h5')

st.title('Predicting the Canceled Quantity of a Product')
st.write('This is a simple web app to predict the canceled quantity of a product based on the input parameters.')

#country = st.selectbox("select you country :" ,
 #                      ('United Kingdom' , 'Germany' , 'France' , 'Spain' , 'Italy' , 'Finland' , 'Malta' , 'USA' , 'EIRA' , 'Japan' ,
  #                      'Poland' ,'RSA' , 'Canada' , 'Sweden' ,'Lithuania' , 'Channel Islands' , 'Cyprus' , 'Switzerland' ,
   #                     'Portugal' , 'Australia')
    #                   )
#st.write('You selected this option :', country)
#id = st.number_input('Enter the Customer ID :')
#stock_code = st.number_input('Enter the Stock Code :')
#date = st.date_input('Enter the Date :')
quantity = st.number_input('Enter the quantity :')

data = [quantity]
data_scaled = scaler.fit_transform([data])
result = model.predict(data_scaled)

st.write('The predicted canceled quantity is :', result)