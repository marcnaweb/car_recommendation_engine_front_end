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
        # if not car_code_row.empty:
        #     car_code = car_code_row.loc['car_code']
        #     # The car_code is now stored in the variable and can be used for your API or any other purpose
        #     st.markdown(f"Car Code: `{car_code}`", unsafe_allow_html=True)
        # else:
        #     st.write("Car code not found.")
car_manufacturer=car_code_row['car_manufacturer']
car_model=car_code_row['car_model']
car_model_year=car_code_row['car_model_year']

current_directory = os.path.dirname(os.path.realpath(__file__))

car_prices_relative_path = os.path.join(current_directory, 'nika_data', 'car_prices_w_prices_scaled.csv')
car_features_relative_path = os.path.join(current_directory, 'nika_data', 'scaled_cleaned.csv')

features_df = pd.read_csv(car_features_relative_path)
price_df = pd.read_csv(car_prices_relative_path)

merged_df = price_df.merge(features_df, left_on="car_code", right_on="car_code", how="left")

search_df = merged_df[["car_manufacturer", "car_model", "car_model_year", "car_code"]].drop_duplicates()


# Function to get car code
def get_car_code(car_manufacturer, car_model, car_model_year, df):
    filtered_df = df[(df['car_manufacturer'] == car_manufacturer) &
                     (df['car_model'] == car_model) &
                     (df['car_model_year'] == car_model_year)]
    if not filtered_df.empty:
        return filtered_df.iloc[0]['car_code']
    else:
        return None

# Streamlit app
def main():
    st.title("Car Code Search")

    # Inputs
    car_manufacturer = st.text_input("Car Manufacturer")
    car_model = st.text_input("Car Model")
    car_model_year = st.number_input("Car Model Year", min_value=1900, max_value=9999)

    # Button to search for car code
    if st.button("Search"):
        # Get the car code
        car_code = get_car_code(car_manufacturer, car_model, car_model_year, search_df)
        car_code = 2707
        if car_code is not None:
            st.success(f"Car Code: {car_code}")

            # Send car code to API
            # Replace 'api_endpoint' with your actual API endpoint
            URL = 'http://127.0.0.1:8000/car_predict/'
            full_url = f"{URL}{car_code}"
            #payload = {'car_code': car_code}
            response = requests.get(full_url)
            data = response.json()
            if response.status_code == 200:
                st.success("Car code sent to API successfully!")
                # answer = response['prediction']
                st.write("API Response:", data["Original_car"])
            else:
                st.error("Failed to send car code to API.")
        else:
            st.error("A car has not been found. Please check the spelling or try different inputs.")

if __name__ == "__main__":
    main()
