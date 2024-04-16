import streamlit as st

# st.set_page_config(
#     page_title="Multipage App",
#     page_icon="✌"
# )

import streamlit as st
import pandas as pd
import requests
import pydeck as pdk
import os
from PIL import Image

#new img function
def searche_img(img_name:str):
    # Your Google Custom Search Engine ID
    cse_id = st.secrets["google_search_cx"]
    # Your API key
    api_key = st.secrets["google_search_key"]
    # The search query
    # query = "auto-data.net " + img_name
    query = "car: " + img_name
    # The search URL
    search_url = f"https://www.googleapis.com/customsearch/v1?q={query}&cx={cse_id}&key={api_key}&searchType=image&num=1"
    # Make the request
    response = requests.get(search_url)
    results = response.json()
    # Extracting image URLs
    try:
        image_urls = [item['link'] for item in results['items']]
        output = image_urls[0]
        return output
    except:
        return("img not working")

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
        background-color: white; /* Pink color */
    }
    </style>
    """,
    unsafe_allow_html=True
)

####################################################################################################################

#IMG
current_directory = os.path.dirname(os.path.realpath(__file__))
img_relative_path = os.path.join(current_directory, 'data', 'final_logo.png')
image = Image.open(img_relative_path)
# st.image(img_relative_path, caption='', width=700)

# This is to keep the image at the centre of the image
with col2:
    st.image(img_relative_path, width=700)



# Add a red horizontal line after the title
st.markdown("<hr style='border:2px solid red'/>", unsafe_allow_html=True)


# # Load the data)
data_path = os.path.join(current_directory, 'data', 'car_features_pr_pred_v2.csv')
data = pd.read_csv(data_path)
data = data[["car_manufacturer", "car_model", "car_model_year", "car_code"]]
data = data.dropna()
data = data.sort_values(['car_manufacturer','car_model', 'car_model_year'])
data["car_model_year"] = data["car_model_year"].astype(int)



################################ Sidebar section####################################################################

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


####################################################################################################################

############################################# user input section ###################################################


# Title
st.markdown("# Car Selection")

# Manufacturer selection with instruction above, sorted alphabetically
st.markdown("### Select a Car Manufacturer", unsafe_allow_html=True)
manufacturers = data['car_manufacturer'].unique()
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
        #selected_year = years[0]



        # Display selected model and year

        # Fetch the car code for the selected model and year for API use (not displayed)
        car_code_row = data[(data['car_manufacturer'] == selected_manufacturer) &
                            (data['car_model'] == selected_model) &
                            (data['car_model_year'] == selected_year)]
        if not car_code_row.empty:
            car_code = car_code_row.iloc[0]['car_code']
        else:
            st.write("Car code not found.")

####################################################################################################################

# Add a red horizontal line after the title
st.markdown("<hr style='border:2px solid red'/>", unsafe_allow_html=True)
# Add a title
st.title("Car Recommendation Engine")
st.markdown("")  # just add little space between title and first button

blal = f"{selected_manufacturer} {selected_model}"
new_link_to_img = searche_img(blal)

if st.button("Predict"):
    if car_code is not None:
        with st.spinner('Working on car models...'):
            # Send car code to API
            URL = 'https://car-recomendation-engine-v2a-d3zpr2mfra-ew.a.run.app/car_predict/'# WORKING ONE
            full_url = f"{URL}{car_code}"
            response = requests.get(full_url)

            # Check if the response was successful
            if response.status_code == 200:
                data = response.json()
                st.success("The car prediction was calculated successfully!")
                st.title('Similar Cars Information')

                st.subheader('Your Car:')
                st.write(f"Manufacturer: ***{data[0]['car_manufacturer']}***")
                st.write(f"Model: ***{data[0]['car_model']}***")
                st.write(f"Car year: ***{int(data[0]['car_model_year'])}***")
                if data[0]['price_pred'] > 1:
                    st.write(f"*Price will decrease by {round(data[0]['price_pred']-1, 2) * 100}%*")
                elif data[0]['price_pred'] == 1:
                    st.write("price will stay as it is")
                else:
                    st.write(f"Car will depreciate approximately by {'{:.1f}'.format(round(1 - data[0]['price_pred'], 2) * 100)}%")
                st.markdown(f'<a href="{new_link_to_img}" target="_blank"><img src="{new_link_to_img}" width="300" height="200"></a>', unsafe_allow_html=True)
                st.markdown("<hr style='border:2px solid red'/>", unsafe_allow_html=True)

                st.subheader('Similar Cars:')
                for car in data[1:]:
                    st.write(f"Manufacturer: ***{car['car_manufacturer']}***")
                    st.write(f"Model: ***{car['car_model']}***")
                    if car['price_pred'] > 1:
                        st.write(f"*Price will decrease by {round(car['price_pred']-1, 2) * 100}%*") # here
                    elif car['price_pred'] == 1:
                        st.write("price will stay as it is")
                    else:
                        st.write(f"Price will decrease by {round(1 - car['price_pred'], 2) * 100}%")
                    images = searche_img(f"{car['car_manufacturer']} {car['car_model']}")
                    if images:
                        st.markdown(f'<a href="{images}" target="_blank"><img src="{images}" width="300" height="200"></a>', unsafe_allow_html=True)
                    else:
                        st.write("No image available")
                    st.write("")  # for a new line between cars
                    st.markdown("<hr style='border:2px solid red'/>", unsafe_allow_html=True)
            else:
                st.error("Failed to send car code to API.")
    else:
        st.error("A car has not been found. Please check the spelling or try different inputs.")
