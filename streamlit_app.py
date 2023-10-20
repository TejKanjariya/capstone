import streamlit as st
import pickle


# Your model loading code (e.g., using joblib, pickle, or your preferred method)
# Load the trained model from the pickle file
model_filename = 'random_forest_model.pkl'
with open(model_filename, 'rb') as model_file:
    model = pickle.load(model_file)


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
