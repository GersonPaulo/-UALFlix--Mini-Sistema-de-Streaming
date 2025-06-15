import streamlit as st
import requests

class HomePage:
    def __init__(self):
        self.endpoints = ["http://127.0.0.1:7000/video_list", "http://192.168.1.74:7000/video_list" ]
        pass

    def fetch_video_list(self):
        for url in self.endpoints:
            try:
                response = requests.get(url, timeout=2)
                if response.status_code == 200:
                    print(response.json())
                    return response.json()
            except Exception as e:
                print(e)
                continue
        return {}

    def genete_containers(self):
        vid_dct = self.fetch_video_list()
        containers_l =  []
        for container in range(len(vid_dct)):
            container = st.container()
            containers_l.append(container)
        return containers_l

    def home_layout(self):
        containers_l = self.genete_containers()
        vid_dct = self.fetch_video_list()
        vid_keys = list(vid_dct.keys())
        i = -1   #porque o len começa do frontend e os index começam do 0
        # CSS para uniformizar os vídeos
        st.markdown("""
                    <style>
                    video {
                        height: 500px !important;
                        width: 100% !important;
                        object-fit: cover;
                        border-radius: 3px;
                        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
                    }
                    </style>
                """, unsafe_allow_html=True)
        for container in containers_l:
            i += 1
            with    container:
                st.video(vid_dct[vid_keys[i]])
                st.write(vid_keys[i])
                if st.button(f"description", key=f"{vid_keys[i]}"):

                    description_txt = ("Este vídeo curto oferece uma experiência visual envolvente, e estão sujeitos "
                                       "a direitos de autor ideal para demonstrações, testes de streaming ou aplicações "
                                       "educacionais. Hospedado em um servidor Flask, o conteúdo é entregue de forma "
                                       "eficiente e pode ser acessado diretamente via navegador.")
                    st.write(description_txt)
                    st.write(f"Duração minima: {5} min")

                else:
                    pass
                st.subheader(" ", divider="gray")

        pass


#logotipo unico da pagina
st.image("images/logo_ualflix.png", width=100)

#titulo da pagina
st.title("Ualflix- Sistema de Streaming")
# espaco entre titulo e header
st.title("                                  ")

# antes do videos


# classe homepage
a = HomePage().home_layout()


