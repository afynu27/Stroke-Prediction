import streamlit as st
import numpy as np
from sklearn.preprocessing import RobustScaler
import joblib
import os
import pandas as pd
import pickle

with open('scaler.pkl', 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)

@st.cache
def load_model(model_file):
    loaded_model = joblib.load(open(os.path.join(model_file),'rb'))
    return loaded_model

def get_data():

    gender = st.radio("Choose your gender", ["Male", "Female"])

    age = st.number_input("Input your age",min_value=0)
    if age < 0:
         st.warning("age must be equal to or above 0")

    hypertension = st.radio("do you have hypertension?", ["Yes", "No"])

    heart_disease = st.radio("do you have heart disease?", ["Yes", "No"])

    ever_married = st.radio("have you ever married?", ["Yes", "No"])

    work_type = st.radio("what type of worker are you?", ["Private","Self-employeed","Goverment_Workers","Children","Never_Worked"])

    residence_type = st.radio("your type of residence", ["Urban", "Rural"])

    avg_glucose_level = st.number_input("input your average glucose level")

    weight = st.number_input("Input your Weight (kg)",min_value = 0.1)
    if weight <= 0:
         st.warning("weight must be above 0")

    height = st.number_input("Input your Height (cm)",min_value=0.1)
    if height <= 0:
         st.warning("height must be above 0")

    if weight <= 0 or height <=0:
         bmi = 0
    else:
        bmi = weight/((height/100)**2)
    st.write("BMI : ",bmi)
    
    smoking_status = st.radio("what type of smoker are you?", ["Formerly_Smoked", "Never_Smoked","Smokes","Unknown"])
    
    user_input = {
        'avg_glucose_level': avg_glucose_level,
        'bmi': bmi,
        'age': age
    }

    user_data = pd.DataFrame(user_input, index=[0])

    user_scaled = scaler.transform(user_data)

    input_feature = np.array([user_scaled[0,2]]+[transform_hypertension[hypertension]]+[transform_heart_disease[heart_disease]]+[user_scaled[0,0]]+[user_scaled[0,1]]+transform_residence_type[residence_type]+transform_ever_married[ever_married]+transform_gender[gender]+transform_smoking_status[smoking_status]+transform_work_type[work_type])

    if st.button("Predict"):
        model = load_model("app_model.pkl")

        prediction = model.predict(input_feature.reshape(1,-1))
        st.write("From the data you have input, you are predicted: ")
        if prediction == 1:
            st.markdown("<div style='text-align: center; font-size: 24px;background-color: RED;'>TO HAVE A STROKE</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div style='text-align: center; font-size: 24px;background-color: green;'>TO BE HEALTHY</div>", unsafe_allow_html=True)

'''Global Variable for categorical data'''
transform_gender = {'Female':[1,0],'Male':[0,1]}
transform_hypertension = {'Yes':1,'No':0}
transform_heart_disease = {'Yes':1,'No':0}
transform_ever_married = {'No':[1,0],'Yes':[0,1]}
transform_work_type = {'Goverment_Workers':[1,0,0,0,0],'Never_Worked':[0,1,0,0,0],'Private':[0,0,1,0,0],'Self-employeed':[0,0,0,1,0],'Children':[0,0,0,0,1]}
transform_residence_type = {'Rural':[1,0],'Urban':[0,1]}
transform_smoking_status = {'Unknown':[1,0,0,0],'Formerly_Smoked':[0,1,0,0],'Never_Smoked':[0,0,1,0],'Smokes':[0,0,0,1]}







