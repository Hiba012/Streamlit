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

if is_active == 'Oui':
    is_active = 1 
else : 0

gender = st.selectbox('Sexe', ('Male', 'Female'))
Géographie = st.selectbox('Géographie', ('France', 'Germany', 'Spain'))

if st.button('Prédire'):
    # Gender
    if gender == 'Female' :
     female = 1
    else : 0

    if gender == 'Male':
        male = 1 
    else : 0

    # Géographie
    if Géographie == 'France' :
       france = 1 
    else: france = 0
    if Géographie == 'Germany':
        germany = 1 
    else: germany = 0
    if Géographie == 'Spain':
        spain = 1 
    else: spain = 0

    features = np.array([[age, balance, num_products, is_active,
                          france, germany, spain,
                          female, male]])

    prediction = model.predict(features)

    # Affichage du résultat
    st.success(f"Résultat de la prédiction : {int(prediction[0])}")