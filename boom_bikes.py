import streamlit as st
import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
import pickle

st.title("Boom Bikes")

st.write(' ### This app predicts the count of bikes based on certain parameters ')

st.sidebar.header('User Input Parameters')

def user_input_features():
	Snow = 0
	Mist = 0
	temp = st.sidebar.slider('Temperature', 2.0 , 35.0)
	windspeed = st.sidebar.slider('Windspeed', 1.0 , 35.0)
	working_day = st.selectbox('Is it a working day?',('Yes','No'))
	if working_day == 'Yes':
		working_day = 1
	else:
		working_day = 0	
	season = st.selectbox('Which season is it?',('Summer','Spring','Winter'))
	if season == 'Summer':
		Summer = 1
		Spring = 0 
		Winter = 0 
	elif season == 'Spring':
		Summer = 0 
		Spring = 1 
		Winter = 0
	else:
		Summer = 0 
		Spring = 0 
		Winter = 1
	weather = st.selectbox('Which type of weather is it?',('Snow','Mist'))			
	if weather == 'Snow':
		Snow = 1
		Mist = 0
	else:
		Mist = 0
		Snow = 1 		
	Year = st.selectbox('Is it 2019?',('Yes', 'No'))
	if Year == 'Yes':
		Year = 1
	else:
		Year = 0
	Sept= st.selectbox('Is it september month?',('Yes','No'))
	if Sept == 'Yes':
		Sept = 1
	else:
		Sept = 0
	data = {'temp': temp,
            'windspeed': windspeed,
            'Spring': Spring,
            'Summer': Summer,
            'Winter': Winter,
            '2019' : Year,
            'mist' : Mist,
            'snow': Snow,
            'sep': Sept,
            'Yes_working': working_day
           }
	       
	features = pd.DataFrame(data, index = [0])
	
	return features

input_df = user_input_features()


boom_bikes_raw = pd.read_csv('Cleaned_Boom_Bikes.csv')

df = pd.concat([input_df,boom_bikes_raw],axis=0)

# Scaling the some of the features
var = ['temp','windspeed']
scaler = MinMaxScaler()
df[var] = scaler.fit_transform(df[var])


input_df_lm = sm.add_constant(df)

st.write(input_df[:1])

pickle_in = open("linear_regression_model.pkl","rb")
regressor = pickle.load(pickle_in)


# Apply model to make predictions
prediction = regressor.predict(input_df_lm[:1])


result=""
if st.button("Predict"):
	result=prediction
st.success('The output is {}'.format(result))
st.write(result) 

