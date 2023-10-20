import streamlit as st
import sklearn
import pickle

# Your model loading code (e.g., using joblib, pickle, or your preferred method)
# Load the trained model from the pickle file
model_filename = 'random_forest_model.pkl'
with open(model_filename, 'rb') as model_file:
    model = pickle.load(model_file)

batting_team =
{'Royal Challengers Bangalore': 0, 'Rising Pune Supergiant': 1, 'Kolkata Knight Riders': 2, 'Kings XI Punjab': 3, 'Delhi Daredevils': 4, 'Sunrisers Hyderabad': 5, 'Mumbai Indians': 6, 'Gujarat Lions': 7, 'Chennai Super Kings': 8, 'Rajasthan Royals': 9, 'Delhi Capitals': 10, 'Deccan Chargers': 11}

bowling_team =
{'Sunrisers Hyderabad': 0, 'Mumbai Indians': 1, 'Gujarat Lions': 2, 'Rising Pune Supergiant': 3, 'Royal Challengers Bangalore': 4, 'Kolkata Knight Riders': 5, 'Delhi Daredevils': 6, 'Kings XI Punjab': 7, 'Rajasthan Royals': 8, 'Chennai Super Kings': 9, 'Delhi Capitals': 10, 'Deccan Chargers': 11}

city =
{'Hyderabad': 0, 'Pune': 1, 'Rajkot': 2, 'Indore': 3, 'Bengaluru': 4, 'Mumbai': 5, 'Kolkata': 6, 'Bangalore': 7, 'Delhi': 8, 'Chandigarh': 9, 'Kanpur': 10, 'Chennai': 11, 'Jaipur': 12, 'Visakhapatnam': 13, 'Abu Dhabi': 14, 'Dubai': 15, 'UAE': 16, 'Ahmedabad': 17, 'Sharjah': 18, 'Navi Mumbai': 19, 'Guwahati': 20, 'Cape Town': 21, 'Port Elizabeth': 22, 'Durban': 23, 'Centurion': 24, 'East London': 25, 'Johannesburg': 26, 'Kimberley': 27, 'Bloemfontein': 28, 'Cuttack': 29, 'Nagpur': 30, 'Dharamsala': 31, 'Raipur': 32, 'Ranchi': 33}

st.title("ML Model Deployment with Streamlit")

# Input elements (10 inputs)
input1 = st.number_input("Input 1")
input2 = st.number_input("Input 2")
# ...
input10 = st.number_input("Input 10")

if st.button("Predict"):
    # Make a prediction using your model
    inputs = [input1, input2, ..., input10]
    # prediction = model.predict(inputs)

    # st.write("Prediction:", prediction)
    st.write("Prediction:- WORK PROGRESS")
