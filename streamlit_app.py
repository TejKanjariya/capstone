import streamlit as st
import sklearn
import pickle
import pandas as pd

# Loading the trained model from the pickle file
model_filename = 'random_forest_model.pkl'
with open(model_filename, 'rb') as model_file:
    model = pickle.load(model_file)

# Read the Excel file into a DataFrame
excel_file = 'ui_player_data.xlsx'
df = pd.read_excel(excel_file)

# Create a dictionary
player_data_dict = {}

# Iterate through the DataFrame and populate the dictionary
for index, row in df.iterrows():
    player_name = row['Player Name']
    total_not_outs = row['Total Not Outs']
    high_score = row['High Score']
    strike_rate = row['Strike Rate']
    
    # Create a list with the three desired columns
    player_data = [total_not_outs, high_score, strike_rate]
    
    # Add the player data list to the dictionary using the player name as the key
    player_data_dict[player_name] = player_data

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
input3 = st.number_input("Input 1")
input4 = st.number_input("Input 2")
input5 = st.number_input("Input 1")
input6 = st.number_input("Input 2")
input7 = st.number_input("Input 1")
input8 = st.number_input("Input 2")
input9 = st.number_input("Input 1")
input10 = st.number_input("Input 10")

if st.button("Predict"):
    # Make a prediction using your model
    inputs = [input1, input2, input3, input4, input5, input6, input7, input8, input9, input10]
    # prediction = model.predict(inputs)

    # st.write("Prediction:", prediction)
    if prediction == 0:
        st.write(f"{input1} will Lose")
    elif prediction == 1:
        st.write(f"{input1} will Win")







