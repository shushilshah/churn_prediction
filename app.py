import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import pickle
from sklearn.preprocessing import StandardScaler


rfc = pickle.load(open('randomforest.pkl', 'rb'))

sclr = StandardScaler()

st.title("Bank Churn Prediction System")


def prediction(credit_score, country, gender, age, tenure, balance, products_number, credit_card, active_member, estimated_salary):
    if credit_score == '':
        st.error("Invalid Input")
        return None
    if country == '':
        st.error("Invalid Input")
        return None
    if gender == '':
        st.error("Invalid Input")
        return None
    if age == '':
        st.error("Invalid Input")
        return None
    if tenure == '':
        st.error("Invalid Input")
        return None
    if balance == '':
        st.error("Invalid Input")
        return None
    if products_number == '':
        st.error("Invalid Input")
        return None
    if credit_card == '':
        st.error("Invalid Input")
        return None
    if active_member == '':
        st.error("Invalid Input")
        return None
    if estimated_salary == '':
        st.error("Invalid Input")
        return None

    features = np.array([[float(credit_score), float(country), gender, float(age), float(tenure), float(
        balance), float(products_number), float(credit_card), float(active_member), float(estimated_salary)]])
    features = sclr.fit_transform(features)
    prediction = rfc.predict(features).reshape(1, -1)
    return prediction[0]


credit_score = st.number_input('Credit score')
country = st.selectbox('Country', [1, 2, 3])
gender = st.selectbox('Gender', [1, 0])
age = st.number_input('Age')
tenure = st.number_input('Tenure')
balance = st.number_input('Balance')
products_number = st.number_input('Products number')
credit_card = st.number_input("Credit Card", min_value=0, max_value=1,)
active_member = st.number_input(
    'Active Member', min_value=0, max_value=1,)
estimated_salary = st.number_input("Entimated Salary")

if st.button('Predict'):
    pred = prediction(credit_score, country, gender, age, tenure, balance,
                      products_number, credit_card, active_member, estimated_salary)

    if pred is not None:
        if pred == 1:
            st.write("The customer has left")

        else:
            st.write("The customer is still active")
