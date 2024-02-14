import streamlit as st
import pandas as pd
import requests
import pydeck as pdk
import os
from PIL import Image

#from serpapi import GoogleSearch  # ignore if serpapi showing error
import requests, lxml
from serpapi import GoogleSearch

# Function for getting image of a car.
def serpapi_get_google_images(query):
    image_results = []

    # search query parameters
    params = {
        "engine": "google",               # search engine. Google, Bing, Yahoo, Naver, Baidu...
        "q": query,                       # search query
        "tbm": "isch",                    # image results
        "num": "10",                     # number of images per page
        "ijn": 0,                         # page number: 0 -> first page, 1 -> second...
        "api_key": "c29d3cb47572955cb027dded55650f88a4520db103243003fa5d897870e405f8",         # https://serpapi.com/manage-api-key
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
    else:
        print(results["error"])
        images_is_present = False

    output = image_results[0]
    return output


############################# Page layout #############################################################
# Set the page to wide mode
st.set_page_config(layout="wide")

# Create three columns
col1, col2, col3 = st.columns([1,2,1])
########################## Background colour section ##############################################################
st.markdown(
    """
    <style>
    /* This sets the background color of the main content area */
    .main .block-container {
        background-color: #f5bcb8; /* Pink color */
    }
    </style>
    """,
    unsafe_allow_html=True
)

####################################################################################################################

#IMG
current_directory = os.path.dirname(os.path.realpath(__file__))
img_relative_path = os.path.join(current_directory, 'data', 'logo.png')
image = Image.open(img_relative_path)
# st.image(img_relative_path, caption='', width=700)

# This is to keep the image at the centre of the image
with col2:
    st.image(img_relative_path, width=700)



# Add a red horizontal line after the title
st.markdown("<hr style='border:2px solid red'/>", unsafe_allow_html=True)


# Load the data
car_prices_relative_path = os.path.join(current_directory, 'nika_data', 'car_prices_w_prices_scaled.csv')
car_features_relative_path = os.path.join(current_directory, 'nika_data', 'scaled_cleaned.csv')

features_df = pd.read_csv(car_features_relative_path)
price_df = pd.read_csv(car_prices_relative_path)

merged_df = price_df.merge(features_df, left_on="car_code", right_on="car_code", how="left")

data = merged_df[["car_manufacturer", "car_model", "car_model_year", "car_code"]].drop_duplicates()
print(data)

################################ Sidebar section####################################################################
# # Sidebar image part


# side_img_relative_path = os.path.join(current_directory, 'data', 'mario-removebg-preview.png')
# side_image = Image.open(side_img_relative_path)

# # Display the image in the sidebar
# st.sidebar.image(side_image, caption='', use_column_width=False, width=200)

# # Add a sidebar section
# # st.sidebar.title("Car Recommendation Engine")

# Custom CSS to inject into the Streamlit page
st.markdown(
    """
    <style>
    .css-1d391kg {
        font-family: 'Helvetica';
        color: #000000;
        font-size: 24px;
        font-weight: 700;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Using the HTML tag directly for the title with the custom style
st.sidebar.markdown(
    '<div class="css-1d391kg">Car Recommendation Engine</div>',
    unsafe_allow_html=True,
)



# You can use markdown to style your text in the sidebar
st.sidebar.markdown("""
## About

Our Car Recommendation Engine is a smart solution designed to simplify your car buying experience.
It uses a predictive pricing model, leveraging a Recurrent Neural Network (RNN) to forecast the future value of vehicles.
This not only helps you understand the long-term investment but also ensures that you find a car that fits within your budget
while accounting for depreciation, fuel costs, insurance, and taxes.

The engine stands out by utilizing unsupervised learning techniques,
including PCA and K-Means clustering, to categorize over 40 different car features into clusters such as 'off-road',
'urban', 'family', or 'sport'. Natural Language Processing (NLP) is also employed to decipher complex car nomenclature,
giving you clear insights into what different car model names and terms actually mean.

Lastly, a unique car grouping and selector feature allows you to prioritize the top characteristics you seek in a vehicle.
The engine then presents you with tailored options, complete with detailed summaries and relevant information,
all powered by advanced AI algorithms. The result is a personalized list of cars that not only match your preferences
but are also a smart financial choice for your future.


""")

####################################################################################################################

############################################# user input section ###################################################


# Title
st.markdown("# Car Selection")

# Manufacturer selection with instruction above, sorted alphabetically
#st.markdown("### Select a Car Manufacturer", unsafe_allow_html=True)
manufacturers = sorted(data['car_manufacturer'].unique())
selected_manufacturer = st.selectbox("**Select a Car Manufacturer**", [""] + manufacturers, key="manufacturer_select")

# Initialize car_code variable
car_code = None

# If a manufacturer is selected, show models for that manufacturer
if selected_manufacturer:
    #st.markdown("### Select a Car Model", unsafe_allow_html=True)

    models = sorted(data[data['car_manufacturer'] == selected_manufacturer]['car_model'].unique())
    selected_model = st.selectbox("**Select a Car Model**", [""] + models, key="model_select")


    # If a model is selected, suggest years
    if selected_model:
        # st.markdown("### Select the Year of the Model", unsafe_allow_html=True)
        years = sorted(data[(data['car_manufacturer'] == selected_manufacturer) &
                            (data['car_model'] == selected_model)]['car_model_year'].unique(), reverse=True)
        #selected_year = st.selectbox("", years, key="year_select")
        selected_year = years[-1]

        # Display selected model and year
        #st.markdown(f"<h2 style='color: green;'>You selected {selected_model}.</h2>", unsafe_allow_html=True)

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

####################################################################################################################

import streamlit as st
import requests

# Your existing code for the Car Selection part goes here

if selected_manufacturer:
    if selected_model:
        # Your code for the second part (Car Recommendation Engine) goes here
        ####################################################################################################################
        # Add a red horizontal line after the title
        st.markdown("<hr style='border:2px solid red'/>", unsafe_allow_html=True)
        # Add a title
        st.title("Car Recommendation Engine")
        st.markdown("")  # just add little space between title and first button

        if st.button(f"You selected {selected_model}. ***(Press to show the image)***"):
            blal = f"{selected_manufacturer} {selected_model}"
            link_to_img = serpapi_get_google_images(blal)
            st.markdown(f'<a href="{link_to_img}" target="_blank"><img src="{link_to_img}" width="300" height="200"></a>', unsafe_allow_html=True)

        if st.button("Predict car depreciation and similar cars"):
            if car_code is not None:
                with st.spinner('Working on car models...'):
                    # Send car code to API
                    URL = 'https://car-recomendation-engine-d3zpr2mfra-ew.a.run.app/car_predict/'
                    full_url = f"{URL}{car_code}"
                    response = requests.get(full_url)

                    # Check if the response was successful
                    if response.status_code == 200:
                        data = response.json()
                        st.success("The car prediction was calculated successfully!")
                        # Display depreciation information
                        st.success(f"Your car will depreciate {round(1 - data['prediction'], 2) * 100}%")

                        # Handling similar cars
                        st.write("Similar cars:")
                        similar_cars = data.get("similar_cars", {})

                        # Optionally remove the first similar car if needed
                        # This part might need adjustment based on your specific requirements
                        if similar_cars:
                            first_key = list(similar_cars.keys())[0]
                            similar_cars.pop(first_key)

                        # Prepare data for display
                        table_data = [{"Manufacturer": manufacturer, "Model": model} for manufacturer, model in similar_cars.items()]

                        # Display the table with similar cars
                        st.table(table_data)
                    else:
                        st.error("Failed to send car code to API.")
            else:
                st.error("A car has not been found. Please check the spelling or try different inputs.")
