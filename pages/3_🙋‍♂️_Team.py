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
    {"name": "Marc", "surname": "Rosenfeld", "picture_url": "https://media.licdn.com/dms/image/C4E03AQEHdperZuI4tQ/profile-displayphoto-shrink_800_800/0/1594160527602?e=1715817600&v=beta&t=IBpRsPKr96it4TSVGPKTrvYdETFfxvV46vqTIhgwegw", "title": "Data Scientist", "linkedin_url": "https://www.linkedin.com/in/marcrosenfeld/", "github_url": "https://github.com/marcnaweb"},
    {"name": "Nikoloz", "surname": "Shubladze", "picture_url": "https://media.licdn.com/dms/image/D4E03AQE1j5QUNY5uJw/profile-displayphoto-shrink_800_800/0/1708612775913?e=1715817600&v=beta&t=VCKmLPnPcKP2CGPoC5npaKT5TdYgoDaemh5pYgGingM", "title": "Data Scientist", "linkedin_url": "https://www.linkedin.com/in/nikolozshubladze/", "github_url": "https://github.com/elnika1"},
    {"name": "Balaji", "surname": "Nalawade", "picture_url": "https://media.licdn.com/dms/image/D5635AQHpJ2eQf-FBFw/profile-framedphoto-shrink_800_800/0/1709228943306?e=1711026000&v=beta&t=6j9ktDozpoVDU8WfBGrLz32Ob6U1ixFMbB3KuTfy4xc", "title": "Data Scientist", "linkedin_url": "https://www.linkedin.com/in/balajinalawade/", "github_url": "https://github.com/bididudy"},
    {"name": "Mahdi", "surname": "Kazemi", "picture_url": "https://media.licdn.com/dms/image/D4E03AQF4sLr-ynlXBw/profile-displayphoto-shrink_800_800/0/1698002313984?e=1715817600&v=beta&t=Vev_68-DyH4PIE1SdhyYAN0natKHTSkn5rwiD6GQ2Hg", "title": "Data Scientist", "linkedin_url": "https://www.linkedin.com/in/m80kaz/", "github_url": "https://github.com/m80kaz"},
    {"name": "Roman", "surname": "Zhvansky", "picture_url": "https://media.licdn.com/dms/image/C5603AQH5G8YTFpOlJw/profile-displayphoto-shrink_800_800/0/1516567019035?e=1715817600&v=beta&t=y6Odu5dJdnch0JaE6t6ozXuc-xivu5ltRXkCI0L3IbI", "title": "Data Scientist", "linkedin_url": "https://www.linkedin.com/in/roman-zhvansky-09379a34/", "github_url": "https://github.com/RomanZhvanskiy"},
    # Add more persons as needed
]

contact_section(persons)
