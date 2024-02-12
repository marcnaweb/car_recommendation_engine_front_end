import pandas as pd
import numpy as np
import os
import requests
import streamlit as st

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
