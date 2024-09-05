# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 06:02:47 2024

@author: Rajpoot
"""


import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('C:/Users\Rajpoot\Desktop/jupyter file/project/trained_model.sav', 'rb'))
def diabeties_prediction(input_data):
    
    data_as_numpy = np.asarray(input_data)
    reshaped_data = data_as_numpy.reshape(1,-1)
    prediction = loaded_model.predict(reshaped_data)
    return prediction
    if (prediction[0]==0):
     return'the patient is no diabaties'
    else:
      return 'the patient is  diabaties'
  
    def mian():
        
        st.title('diabeties prediction web app')
                                             
          
        Pregnancies = st.text_input('enter number od Pregnancies')
        Glucose = st.text_input('enter number od Glucose')
        BloodPressure = st.text_input('enter number od BloodPressure')
        SkinThickness = st.text_input('enter number od SkinThickness')
        Insulin = st.text_input('enter number od Insulin')
        BMI = st.text_input('enter number od BMI')
        DiabetesPedigreeFunction = st.text_input('enter number od DiabetesPedigreeFunction')
        Age = st.text_input('enter number od Age')
        
        diagnosis =''
        
        if st.button('diabetes test results '):
            diagnosis = diabeties_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
            
            st.success(diagnosis)
            
            if __name__ == '__mian__':
                mian()
        
        
        
        
    