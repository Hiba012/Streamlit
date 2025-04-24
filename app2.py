import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.title("Prédiction de Churn Client")
st.write("Bienvenue dans l'application de prédiction de churn client !")
st.write("Veuillez entrer les informations suivantes :")


with open("rf.pkl", "rb") as file:
    model = pickle.load(file)

st.header("Veuillez entrer les informations du client :")

age = st.number_input('Âge', min_value=0, step=1)
balance = st.number_input('Balance bancaire')
num_products = st.number_input('Nombre de produits', min_value=0, max_value=10, step=1)
is_active = st.selectbox('Client actif ', ('Oui', 'Non'))
gender = st.selectbox('Sexe', ('Male', 'Female'))
geography = st.selectbox('Géographie', ('France', 'Germany', 'Spain'))

#is_active :
if is_active == 'Oui':
    is_active = 1 
else : 0
#gender :
gender_val = 1 if gender == 'Male' else 0
#geography :
geography_val = {'France': 0, 'Germany': 1, 'Spain': 2}[geography]

features = np.array([[age, balance, num_products, is_active,
                          geography_val,
                          gender_val]])

prediction = model.predict(features)

# Affichage du résultat
st.success(f"Résultat de la prédiction : {int(prediction[0])}")