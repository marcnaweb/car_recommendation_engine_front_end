import streamlit as st
import pandas as pd
import requests
import pydeck as pdk
import os
from PIL import Image

current_directory = os.path.dirname(os.path.realpath(__file__))
img_relative_path = os.path.join(current_directory, 'data', 'picture_name_here.png')
image = Image.open(img_relative_path)
st.image(img_relative_path, caption='', width=700)

st.title("Car Recommendation Engine")


# Load the data
data_relative_path = os.path.join(current_directory, 'data', 'car_prices_w_prices_scaled.csv')
data = pd.read_csv(data_relative_path)

# Title
st.markdown("# Car Selection")

# Manufacturer selection with instruction above, sorted alphabetically
st.markdown("### Select a Car Manufacturer", unsafe_allow_html=True)
manufacturers = sorted(data['car_manufacturer'].unique())
selected_manufacturer = st.selectbox("", manufacturers, key="manufacturer_select")

# Initialize car_code variable
car_code = None

# If a manufacturer is selected, show models for that manufacturer
if selected_manufacturer:
    st.markdown("### Select a Car Model", unsafe_allow_html=True)
    models = sorted(data[data['car_manufacturer'] == selected_manufacturer]['car_model'].unique())
    selected_model = st.selectbox("", models, key="model_select")

    # If a model is selected, suggest years
    if selected_model:
        st.markdown("### Select the Year of the Model", unsafe_allow_html=True)
        years = sorted(data[(data['car_manufacturer'] == selected_manufacturer) &
                            (data['car_model'] == selected_model)]['car_model_year'].unique(), reverse=True)
        selected_year = st.selectbox("", years, key="year_select")

        # Display selected model and year
        st.markdown(f"<h2 style='color: green;'>You selected {selected_model} from {selected_year}.</h2>", unsafe_allow_html=True)

        # Fetch the car code for the selected model and year for API use (not displayed)
        car_code_row = data[(data['car_manufacturer'] == selected_manufacturer) &
                            (data['car_model'] == selected_model) &
                            (data['car_model_year'] == selected_year)]
        if not car_code_row.empty:
            car_code = car_code_row.iloc[0]['car_code']
            # The car_code is now stored in the variable and can be used for your API or any other purpose
            st.markdown(f"Car Code: `{car_code}`", unsafe_allow_html=True)
        else:
            st.write("Car code not found.")
