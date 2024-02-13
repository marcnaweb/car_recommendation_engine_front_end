import streamlit as st
import pandas as pd
import requests
import pydeck as pdk
import os
from PIL import Image


from serpapi import GoogleSearch
import requests, lxml, re, json, urllib.request


def serpapi_get_google_images(query):
    image_results = []

    # search query parameters
    params = {
        "engine": "google",               # search engine. Google, Bing, Yahoo, Naver, Baidu...
        "q": query,                       # search query
        "tbm": "isch",                    # image results
        "num": "10",                     # number of images per page
        "ijn": 0,                         # page number: 0 -> first page, 1 -> second...
        "api_key": "c29d3cb47572955cb027dded55650f88a4520db103243003fa5d897870e405f8",                 # https://serpapi.com/manage-api-key
        # other query parameters: hl (lang), gl (country), etc
    }

    search = GoogleSearch(params)         # where data extraction happens

    images_is_present = True
    #while images_is_present:
    results = search.get_dict()       # JSON -> Python dictionary

    # checks for "Google hasn't returned any results for this query."
    if "error" not in results:
        for index, image in enumerate(results["images_results"], start=1):
            if image["original"] not in image_results:
                image_results.append(image["original"])
                if index>2:
                    break

        # update to the next page
        #params["ijn"] += 1
    else:
        print(results["error"])
        images_is_present = False

    # -----------------------
    # Downloading images
    # for index, image in enumerate(image_results, start=1):
    #     print(f"Downloading {index} image...")

    #     opener=urllib.request.build_opener()
    #     opener.addheaders=[("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36")]
    #     urllib.request.install_opener(opener)

    #     urllib.request.urlretrieve(image, f"{query}_{index}.jpg")

    #     if index>2:
    #         break

    output = image_results[0]
    return output

    # print(json.dumps(image_results, indent=2))
    # print(len(image_results))

def main():
    #IMG
    current_directory = os.path.dirname(os.path.realpath(__file__))
    img_relative_path = os.path.join(current_directory, 'data', 'picture_name_here.png')
    image = Image.open(img_relative_path)
    st.image(img_relative_path, caption='', width=700)

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
            # st.markdown("### Select the Year of the Model", unsafe_allow_html=True)
            years = sorted(data[(data['car_manufacturer'] == selected_manufacturer) &
                                (data['car_model'] == selected_model)]['car_model_year'].unique(), reverse=True)
            #selected_year = st.selectbox("", years, key="year_select")
            selected_year = years[-1]
            st.title("Car Recommendation Engine")
            # Display selected model and year
            #st.success(f"You selected {selected_model}.")

            # Fetch the car code for the selected model and year for API use (not displayed)
            car_code_row = data[(data['car_manufacturer'] == selected_manufacturer) &
                                (data['car_model'] == selected_model) &
                                (data['car_model_year'] == selected_year)]
            if not car_code_row.empty:
                car_code = car_code_row.iloc[0]['car_code']

                # The car_code is now stored in the variable and can be used for your API or any other purpose
                # st.markdown(f"Car Code: `{car_code}`", unsafe_allow_html=True) # show car code for testing purpose
            else:
                st.write("Car code not found.")

    if st.button(f"You selected {selected_model}. ***(Press to show the image)***"):
        blal = f"{selected_manufacturer} {selected_model}"
        link_to_img = serpapi_get_google_images(blal)
        st.markdown(f'<a href="{link_to_img}" target="_blank"><img src="{link_to_img}" width="300" height="200"></a>', unsafe_allow_html=True)

    if st.button("Predict car depriciation and similar cars"):
        if car_code is not None:
            #st.success(f"Car Code: {car_code}") #Showing car code for testing

            # Send car code to API
            URL = 'https://car-recomendation-engine-d3zpr2mfra-ew.a.run.app/car_predict/'
            full_url = f"{URL}{car_code}"
            response = requests.get(full_url)
            data = response.json()
            if response.status_code == 200:
                st.success("The car prediction was calculated successfully!")
                # answer = response['prediction']
                # st.write("API Response:", data["Original_car"])
                st.success(f"Your car will depriciate {round(1 - data['prediction'],2)}%")
                st.write("Similar cars:")
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


if __name__ == "__main__":
    main()














# current_directory = os.path.dirname(os.path.realpath(__file__))

# car_prices_relative_path = os.path.join(current_directory, 'nika_data', 'car_prices_w_prices_scaled.csv')
# car_features_relative_path = os.path.join(current_directory, 'nika_data', 'scaled_cleaned.csv')

# features_df = pd.read_csv(car_features_relative_path)
# price_df = pd.read_csv(car_prices_relative_path)

# merged_df = price_df.merge(features_df, left_on="car_code", right_on="car_code", how="left")

# search_df = merged_df[["car_manufacturer", "car_model", "car_model_year", "car_code"]].drop_duplicates()
# print(search_df[['car_model']].unique.count())


# # Function to get car code
# def get_car_code(car_manufacturer, car_model, car_model_year, df):
#     filtered_df = df[(df['car_manufacturer'] == car_manufacturer) &
#                      (df['car_model'] == car_model) &
#                      (df['car_model_year'] == car_model_year)]
#     if not filtered_df.empty:
#         return filtered_df.iloc[0]['car_code']
#     else:
#         return None

# # Streamlit app
# def main():
#     st.title("Car Code Search")

#     # Inputs
#     car_manufacturer = st.text_input("Car Manufacturer")
#     car_model = st.text_input("Car Model")
#     car_model_year = st.number_input("Car Model Year", min_value=1900, max_value=9999)

#     # Button to search for car code
#     if st.button("Search"):
#         # Get the car code
#         car_code = get_car_code(car_manufacturer, car_model, car_model_year, search_df)
#         car_code = 2707
#         if car_code is not None:
#             st.success(f"Car Code: {car_code}")

#             # Send car code to API
#             # Replace 'api_endpoint' with your actual API endpoint
#             URL = 'http://127.0.0.1:8000/car_predict/'
#             full_url = f"{URL}{car_code}"
#             #payload = {'car_code': car_code}
#             response = requests.get(full_url)
#             data = response.json()
#             if response.status_code == 200:
#                 st.success("Car code sent to API successfully!")
#                 # answer = response['prediction']
#                 st.write("API Response:", data["Original_car"])
#             else:
#                 st.error("Failed to send car code to API.")
#         else:
#             st.error("A car has not been found. Please check the spelling or try different inputs.")

# if __name__ == "__main__":
#     main()
