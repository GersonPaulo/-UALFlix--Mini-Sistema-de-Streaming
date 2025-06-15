import streamlit as st
import requests

FLASK_ENDPOINTS = [
    "http://127.0.0.1:7000/video_list",
    "http://192.168.1.74:7000/video_list",  # Replace with your LAN IP
]


def fetch_video_list():
    for url in FLASK_ENDPOINTS:
        try:
            response = requests.get(url, timeout=2)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(e)
            continue
    return {}
# Set Streamlit page config


# Dictionary of available videos (you can add more)
videos = fetch_video_list()
vd_keys = list(videos.keys())
st.image("images/logo_ualflix.png", width=100)
st.title("UALFlix- Mini Sistema de Streaming")

if videos:
    # Select box to choose video

    choice = st.selectbox("Video para assistir:", list(videos.keys()))
    st.markdown("""
                <style>
                video {
                    height: 500px !important;
                    width: 100% !important;
                    object-fit: cover;
                    border-radius: 5px;
                    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
                }
                </style>
            """, unsafe_allow_html=True)
    if choice:
        # Display the selected video
        st.video(videos[choice])
        if st.button(f"Sinopse"):
            view_count = 0

            st.write(f"{choice}")
            description_txt = ("Este vídeo curto oferece uma experiência visual envolvente, e estão sujeitos "
                               "a direitos de autor ideal para demonstrações, testes de streaming ou aplicações "
                               "educacionais. Hospedado em um servidor Flask, o conteúdo é entregue de forma "
                               "eficiente e pode ser acessado diretamente via navegador.")
            st.write(description_txt)
            st.write(f"Duração minima: {5} min")




else:
    st.error("No videos found. Is the Flask server running?")



#to run the to run file we put in terminal streamlit run  filename
#exemplo streamlit run .\test_streamlit.py
