import streamlit as st
import pandas as pd
import requests
import pydeck as pdk
import os
from PIL import Image

#IMG
current_directory = os.path.dirname(os.path.realpath(__file__))
img_relative_path = os.path.join(current_directory, 'data', 'picture_name_here.png')
image = Image.open(img_relative_path)
st.image(img_relative_path, caption='', width=700)

st.title("Car Recommendation Engine")


# Load the data
car_prices_relative_path = os.path.join(current_directory, 'nika_data', 'car_prices_w_prices_scaled.csv')
car_features_relative_path = os.path.join(current_directory, 'nika_data', 'scaled_cleaned.csv')

features_df = pd.read_csv(car_features_relative_path)
price_df = pd.read_csv(car_prices_relative_path)

merged_df = price_df.merge(features_df, left_on="car_code", right_on="car_code", how="left")

data = merged_df[["car_manufacturer", "car_model", "car_model_year", "car_code"]].drop_duplicates()
print(data)

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
        #selected_year = st.selectbox("", years, key="year_select")
        selected_year = years[-1]

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

if st.button("Search"):
    if car_code is not None:
        st.success(f"Car Code: {car_code}")

        # Send car code to API
        # Replace 'api_endpoint' with your actual API endpoint
        URL = 'https://car-recomendation-engine-d3zpr2mfra-ew.a.run.app/car_predict/'
        full_url = f"{URL}{car_code}"
        response = requests.get(full_url)
        data = response.json()
        if response.status_code == 200:
            st.success("Car code sent to API successfully!")
            # answer = response['prediction']
            # st.write("API Response:", data["Original_car"])
            st.write(f"Your car will loose {round(1 - data['prediction'],2)}%")
            st.write("Simular cars:")
            similar_cars = data.get("similar_cars", {})

            # Remove the first key-value pair from the "similar_cars" dictionary
            if similar_cars:
                first_key = list(similar_cars.keys())[0]
                similar_cars.pop(first_key)

            # st.write(f"{similar_cars}")

            # Convert the similar_cars dictionary to a list of tuples
            table_data = [{"Manufacturer": manufacturer, "Model": model} for manufacturer, model in similar_cars.items()]


            # Display the table
            st.table(table_data)

        else:
            st.error("Failed to send car code to API.")
    else:
        st.error("A car has not been found. Please check the spelling or try different inputs.")
