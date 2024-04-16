import streamlit as st

st.title("About")

st.markdown(
    """
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
    """
)
