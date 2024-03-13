import streamlit as st

# st.title("Contact")

import streamlit as st

def contact_section(persons):
    st.markdown("<h1 style='text-align: center;'>Contact</h1>", unsafe_allow_html=True)

    # Horizontal scrollable container
    st.write('<div style="overflow-x: auto; white-space: nowrap;">', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    for i, person in enumerate(persons):
        if i % 3 == 0:
            contact_col = col1
        elif i % 3 == 1:
            contact_col = col2
        else:
            contact_col = col3

        with contact_col:
            st.markdown('<div style="display: inline-block; margin: 20px; text-align: center;">', unsafe_allow_html=True)
            st.markdown(f'<img src="{person["picture_url"]}" alt="{person["name"]} {person["surname"]}" style="width: 150px; height: 150px; border-radius: 50%;">', unsafe_allow_html=True)
            st.markdown(f"<h2>{person['name']} {person['surname']}</h2>", unsafe_allow_html=True)
            st.markdown(f'<p><b>Title:</b> {person["title"]}</p>', unsafe_allow_html=True)
            st.markdown(f'<p><a href="{person["linkedin_url"]}" target="_blank">LinkedIn</a></p>', unsafe_allow_html=True)
            st.markdown(f'<p><a href="{person["github_url"]}" target="_blank">GitHub</a></p>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    st.write('</div>', unsafe_allow_html=True)

# Example usage with multiple persons
persons = [
    {"name": "John", "surname": "Doe", "picture_url": "john_picture.jpg", "title": "Data Scientist", "linkedin_url": "https://www.linkedin.com/in/johndoe", "github_url": "https://github.com/johndoe"},
    {"name": "Jane", "surname": "Smith", "picture_url": "jane_picture.jpg", "title": "Software Engineer", "linkedin_url": "https://www.linkedin.com/in/janesmith", "github_url": "https://github.com/janesmith"},
    {"name": "kola", "surname": "rosberg", "picture_url": "jane_picture.jpg", "title": "Software Engineer", "linkedin_url": "https://www.linkedin.com/in/janesmith", "github_url": "https://github.com/janesmith"},
    {"name": "Jane", "surname": "Smith", "picture_url": "jane_picture.jpg", "title": "Software Engineer", "linkedin_url": "https://www.linkedin.com/in/janesmith", "github_url": "https://github.com/janesmith"},
    {"name": "Jane", "surname": "Smith", "picture_url": "jane_picture.jpg", "title": "Software Engineer", "linkedin_url": "https://www.linkedin.com/in/janesmith", "github_url": "https://github.com/janesmith"},
    # Add more persons as needed
]

contact_section(persons)
