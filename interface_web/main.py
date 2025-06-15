import streamlit as st

# logotipo
st.set_page_config(page_title="Ualflix", page_icon="images/logo_ualflix.png", layout="wide")
st.sidebar.image("images/logo_ualflix.png", width=150)


def main():

    st.image("images/logo_ualflix.png", width=100)
    st.title("Criador Gerson Gonçalves")

    col1, col2, col3 = st.columns([3, 3, 3])
    with col1:
        st.image("images/igor1.jpg")
    with col2:
        st.image("images/igor2.jpg")
    with col3:
        st.image("images/igor3.jpg")
    st.subheader("Dedicatória ao Criador da UALFLIX")
    st.write("Quero dedicar estas palavras ao visionário por trás da UALFLIX, Igor Gerson Gonçalves Paulo, conhecido"
             "artisticamente como Gerson Patrick. Jovem angolano de 24 anos, estudante finalista do curso de Engenharia "
             "Informática na Universidade Autónoma de Lisboa, solteiro e temente a Deus, Gerson é exemplo de dedicação,"
             " fé e criatividade. ")
    st.write("A sua jornada inspira todos nós que acreditamos no poder da educação, da inovação e da persistência."
             " Que este projeto seja apenas o começo de muitas conquistas!Com admiração.")
    st.write("Gerson Patrick")

pg = st.navigation(["homepage.py", "test_streamlit.py", "pagina1.py", "pagina2.py", "upload.py", main])
pg.run()

#to run the to run file we put in terminal streamlit run  filename
#exemplo streamlit run .\test_streamlit.py
