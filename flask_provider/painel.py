import streamlit as st
import requests
import os




class Painel():
    def __init__(self):
        self.save_folder = r"C:\Users\igorp\OneDrive\Documentos\docker_test1\flask_provider\vids_flask"
        self.endpoints = ["http://192.168.1.74:7000/video_list", "http://127.0.0.1:7000/video_list"]
        pass

    #combina o nome dos files com os endpoinst flask local and 192 porta 7000
    def fetch_video_list(self):
        for url in self.endpoints:
            try:
                response = requests.get(url, timeout=2)
                if response.status_code == 200:
                    return response.json()
            except Exception as e:
                print(e)
                continue
        return {}

    # retorna true if type is the same as required
    def is_file_type(self, file, expected_ext):
        extension = os.path.splitext(file)[1].lower()  # Garante que a extensão esteja em minúsculas
        return extension == f".{expected_ext.lower()}"  # Compara com o formato correto

    # Processa e salva cada arquivo
    def uploads(self):
        uploaded_file = st.file_uploader("Choose a Video")
        if uploaded_file is not None:
            if self.is_file_type(uploaded_file.name, "mp4"):
                file_path = os.path.join(self.save_folder, uploaded_file.name)
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.read())
                st.write("filename:", uploaded_file.name)
            else:
                st.write("ficheiro Invalido :", uploaded_file.name)
        else:
            pass
        # Lista os arquivos salvos
        if st.button(f"Arquivos salvos na pasta"):
            st.write("Arquivos salvos na pasta:")
            st.write(os.listdir(self.save_folder))

        #mostra um link direto para os videos
        if st.button(f"Link direto dos videos:"):
            videos = self.fetch_video_list()
            vid_names = list(videos.keys())
            i =0
            for links in list(videos.values()):
                i+=1
                st.write(f"{vid_names[i]}:")
                st.subheader(links.replace(" ", "%20"))



# logotipo
st.set_page_config(page_title="Ualflix", page_icon="images/logo_ualflix.png", layout="wide")
st.sidebar.image("images/logo_ualflix.png", width=150)
st.sidebar.subheader("ADM")
st.image("images/logo_ualflix.png", width=100) #logotipo unico da pagina
st.title("Ualflix  Painel administrativo simples") #titulo da pagina
st.title(""         ""       ""         "") # espaco entre titulo e header
st.header(f"ADM ")# texto antes do coteudo

# Caminho absoluto onde os arquivos serão salvos

painel_run = Painel().uploads()