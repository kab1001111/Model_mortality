import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import joblib

# Cargar datos
df = pd.read_csv("dfcleaned.csv")

# Cargar modelo
model = joblib.load("modelo.pkl")

# Crear interfaz de usuario
st.header("Modelo Predictivo de Mortalidad")
st.write("Ingrese los los datos del paciente:")
var_1 = st.slider("Gender", 0, 10, 5)
var_2 = st.slider("Blood", 0, 10, 5)
var_3 = st.slider("Circulatory", 0, 10, 5)
var_4 = st.slider("Congenital", 0, 10, 5 )
var_5 = st.slider("Digestive", 0, 10, 5)
var_6 = st.slider("Endocrine", 0, 10, 5)
var_7 = st.slider("Genitourinary", 0, 10, 5)
var_8 = st.slider("Infectius", 0, 10, 5)
var_9 = st.slider("Injury", 0, 10, 5)
var_10 = st.slider("Mental", 0, 10, 5)
var_11 = st.slider("Misc", 0, 10, 5)
var_12 = st.slider("Muscular", 0, 10, 5)
var_13 = st.slider('Neoplasm', 0, 10, 5)
var_14 = st.slider("Nervous", 0, 10, 5)
var_15 = st.slider("Prenatal", 0, 10, 5)
var_16 = st.slider("Respiratory", 0, 10, 5)
var_17 = st.slider("Skin", 0, 10, 5)
var_18 = st.slider("Coronay", 0, 10, 5)
var_19 = st.slider("Coranary Care Unit", 0, 10, 5)
var_20 = st.slider("Cardiac Sugery Recovery", 0, 10, 5)
var_21 = st.slider("Medical Intensive Care", 0, 10, 5)
var_22 = st.slider("Surgical Intensive", 0, 10, 5)
var_23 = st.slider("Trauma", 0, 10, 5)
var_24 = st.slider("Variable 24", 0, 10, 5)
var_25 = st.slider("Variable 25", 0, 10, 5)
var_26 = st.slider("Etnia Afro", 0, 10, 5)
var_27 = st.slider("Etnia hispana", 0, 10, 5)
var_28 = st.slider("Etnia other 26", 0, 10, 5)
var_29= st.slider("Etnia blanca", 0, 1)
var_30 = st.slider("Age_Meddle", 0, 10, 5)



# Realizar predicción
input_data = np.array([[var_1, var_2, var_3,var_4,var_5, var_6,var_7,
                        var_8,var_9,var_10,var_11,var_12,var_13,var_14,
                        var_15,var_16,var_17,var_18,var_19,var_20,var_21,
                        var_22,var_23,var_24,var_25,var_26,var_27,var_28,
                        var_29,var_30
                        ]]) 
                      
prediction = model.predict(input_data)

# Mostrar resultados
st.subheader("Resultado:")
if prediction == 1:
    st.write("El paciente tiene alta probabilidad de morir.")
else:
    st.write("El paciente tiene baja probabilidad de morir.")
