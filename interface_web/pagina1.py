from symtable import Class

import streamlit as st
from homepage import HomePage


class PaginaUm:
    def __init__(self):
        pass

    def layout_columns(self):
        vid_dct = HomePage().fetch_video_list()
        vid_keys = list(vid_dct.keys())

        a = 0
        for i in range(0, len(vid_keys),2) :
            col1,  col2= st.columns([2, 2])

            with col1:
                st.image("images/play_thumbnail.png", width=180)
                st.write(vid_keys[a - 1])
                if st.button(f"play", a):
                    st.video(vid_dct[vid_keys[a-1]])
                    st.write(vid_keys[a-1])
                    description_txt = ("Este vídeo curto oferece uma experiência visual envolvente, e estão sujeitos "
                                       "a direitos de autor ideal para demonstrações, testes de streaming ou aplicações "
                                       "educacionais. Hospedado em um servidor Flask, o conteúdo é entregue de forma "
                                       "eficiente e pode ser acessado diretamente via navegador.")
                    st.write(description_txt)
                    st.write(f"Duração minima: {5} min")

            with col2:
                st.image("images/play_thumbnail.png", width=180)
                st.write(vid_keys[a])
                if st.button(f"play", a+1):
                    st.video(vid_dct[vid_keys[a]])
                    description_txt = ("Este vídeo curto oferece uma experiência visual envolvente, e estão sujeitos "
                                       "a direitos de autor ideal para demonstrações, testes de streaming ou aplicações "
                                       "educacionais. Hospedado em um servidor Flask, o conteúdo é entregue de forma "
                                       "eficiente e pode ser acessado diretamente via navegador.")
                    st.write(description_txt)
                    st.write(f"Duração minima: {5} min")

            st.subheader(" ", divider="gray")
            a += 2



        pass

#logotipo unico da pagina
st.image("images/logo_ualflix.png", width=100)

#titulo da pagina
st.title("Ualflix- Sistema de Streaming")

# espaco entre titulo e header
st.title(""         ""       ""         "")

# antes do videos

pg1_run = PaginaUm().layout_columns()
