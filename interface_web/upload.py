import streamlit as st
import os



st.image("images/logo_ualflix.png", width=100) #logotipo unico da pagina
st.title("Ualflix  Painel administrativo simples") #titulo da pagina
st.title(""         ""       ""         "") # espaco entre titulo e header
st.header(f"Add New Videos adm IGOR only")# texto antes do coteudo

# Caminho absoluto onde os arquivos serão salvos
save_folder = r"C:\Users\igorp\OneDrive\Documentos\docker_test1\flask_provider\vids_flask"

# Upload de múltiplo arquivo
uploaded_file = st.file_uploader("Choose a Video")

#retorna true if type is the same as required
def is_file_type(file, expected_ext):
    extension = os.path.splitext(file)[1].lower()  # Garante que a extensão esteja em minúsculas
    return extension == f".{expected_ext.lower()}"  # Compara com o formato correto

# Processa e salva cada arquivo

if uploaded_file is not None:
    if  is_file_type(uploaded_file.name , "mp4"):
        file_path = os.path.join(save_folder, uploaded_file.name)
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
    st.write(os.listdir(save_folder))



