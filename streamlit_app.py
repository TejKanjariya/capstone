import streamlit as st
import pickle
import pandas as pd

# Loading the trained model from the pickle file
model_filename = 'random_forest_model.pkl'
with open(model_filename, 'rb') as model_file:
    model = pickle.load(model_file)

# # Load the trained neural model
# with open('neural_network_model.pkl', 'rb') as neural_model_file:
#     neural_model = pickle.load(neural_model_file)

# Read the Excel file into a DataFrame
excel_file = 'ui_player_data.xlsx'
df = pd.read_excel(excel_file)

# Create a dictionary
player_data_dict = {}

# Iterate through the DataFrame and populate the dictionary
for index, row in df.iterrows():
    player_name = row['Player Name']
    total_not_outs = row['Total Not Outs']
    high_score = row['Highest Score']
    strike_rate = row['Strike Rate']

    # Create a list with the three desired columns
    player_data = [total_not_outs, high_score, strike_rate]

    # Add the player data list to the dictionary using the player name as the key
    player_data_dict[player_name] = player_data

batting_team = {
    'Royal Challengers Bangalore': 0,
    'Rising Pune Supergiant': 1,
    'Kolkata Knight Riders': 2,
    'Kings XI Punjab': 3,
    'Delhi Daredevils': 4,
    'Sunrisers Hyderabad': 5,
    'Mumbai Indians': 6,
    'Gujarat Lions': 7,
    'Chennai Super Kings': 8,
    'Rajasthan Royals': 9,
    'Delhi Capitals': 10,
    'Deccan Chargers': 11
}

bowling_team = {
    'Sunrisers Hyderabad': 0,
    'Mumbai Indians': 1,
    'Gujarat Lions': 2,
    'Rising Pune Supergiant': 3,
    'Royal Challengers Bangalore': 4,
    'Kolkata Knight Riders': 5,
    'Delhi Daredevils': 6,
    'Kings XI Punjab': 7,
    'Rajasthan Royals': 8,
    'Chennai Super Kings': 9,
    'Delhi Capitals': 10,
    'Deccan Chargers': 11
}

city = {
    'Hyderabad': 0,
    'Pune': 1,
    'Rajkot': 2,
    'Indore': 3,
    'Bengaluru': 4,
    'Mumbai': 5,
    'Kolkata': 6,
    'Bangalore': 7,
    'Delhi': 8,
    'Chandigarh': 9,
    'Kanpur': 10,
    'Chennai': 11,
    'Jaipur': 12,
    'Visakhapatnam': 13,
    'Abu Dhabi': 14,
    'Dubai': 15,
    'UAE': 16,
    'Ahmedabad': 17,
    'Sharjah': 18,
    'Navi Mumbai': 19,
    'Guwahati': 20,
    'Cape Town': 21,
    'Port Elizabeth': 22,
    'Durban': 23,
    'Centurion': 24,
    'East London': 25,
    'Johannesburg': 26,
    'Kimberley': 27,
    'Bloemfontein': 28,
    'Cuttack': 29,
    'Nagpur': 30,
    'Dharamsala': 31,
    'Raipur': 32,
    'Ranchi': 33
}

st.title("ML Model Deployment with Streamlit")

# Input elements (10 inputs)
# input1 = st.selectbox("Select Batting Team", list(batting_team.keys()))
# input2 = st.selectbox("Select Bowling Team", list(bowling_team.keys()))
# input3 = st.selectbox("Select City", list(city.keys()))
input4 = st.selectbox("Select Current Batsman", list(player_data_dict.keys()))
input41 = st.selectbox("Select Current Over", min_value=0, max_value=10, value=0, step=1)
input42 = st.selectbox("Select Current Ball", min_value=0, max_value=10, value=0, step=1)
# input5 = st.number_input("Input 5", min_value=0, max_value=10, value=0, step=1)
# input6 = st.number_input("Input 6", min_value=0, max_value=10, value=0, step=1)
# input7 = st.number_input("Input 7", min_value=0, max_value=10, value=0, step=1)
# input8 = st.number_input("Input 8", value=0.0)
# input9 = st.number_input("Input 9", value=0.0)
# input10 = st.slider("Input 10", min_value=0, max_value=10, value=5)
# neural_input = [input41, input42, player_data_dict[input4][1], player_data_dict[input4][2], player_data_dict[input4][0]]
H1 = max(0, 0.9110675 * input41 - 0.03449272 * input42 + 1.0922453 * player_data_dict[input4][1] + 0.6379537 * player_data_dict[input4][2] - 0.6832345 * player_data_dict[input4][0])
H2 = max(0, 0.34656823 * input41 - 0.7189315 * input42 + 0.26758012 * player_data_dict[input4][1] + 0.02426003 * player_data_dict[input4][2] - 0.70526344 * player_data_dict[input4][0])
H3 = max(0, -1.5374088 * input41 + 0.046777 * input42 + 1.6355581 * player_data_dict[input4][1] - 1.8444831 * player_data_dict[input4][2] - 0.8660773 * player_data_dict[input4][0])
H4 = max(0, 0.4858154 * input41 + 0.07428534 * input42 + 0.6507748 * player_data_dict[input4][1] + 0.7169861 * player_data_dict[input4][2] + 0.3320721 * player_data_dict[input4][0])
H5 = max(0, 0.42746195 * input41 + 0.16714458 * input42 + 0.35787955 * player_data_dict[input4][1] + 0.20249411 * player_data_dict[input4][2] + 0.17194664 * player_data_dict[input4][0])

output = -2.0390031 * H1 - 0.65763295 * H2 + 2.231145 * H3 - 2.4533222 * H4 + 0.27485844 * H5

# neural_input = pd.DataFrame({'Over': [input41], 'Delivery': [input42], 'high_score_class': [player_data_dict[input4][1]], 'strike_class': [player_data_dict[input4][2]], 'not_out_class': [player_data_dict[input4][0]]})
# print("input here :-", neural_input)
if st.button("Predict"):
    # Map selected values to their respective integer values
    # input1 = batting_team[input1]
    # input2 = bowling_team[input2]
    # input3 = city[input3]
    # input4 = player_data_dict[input4]

    # Make a prediction using your model
    # inputs = [input1, input2, input3, input4, input5, input6, input7, input8, input9, input10]
    # prediction = neural_model.predict([neural_input])
    # st.write("neural prediction :-", prediction)
    st.write("neural prediction :-", output)
    # if prediction == 0:
    #     st.write("The team will Lose")
    # elif prediction == 1:
    #     st.write("The team will Win")
