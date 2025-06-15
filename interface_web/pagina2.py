import streamlit as st
from homepage import HomePage


class PaginaDois:
    def __init__(self):
        pass

    def layout_columns(self):
        vid_dct = HomePage().fetch_video_list()
        vid_keys = list(vid_dct.keys())
        a = 0
        # CSS para uniformizar os vídeos
        st.markdown("""
            <style>
            video {
                height: 300px !important;
                width: 100% !important;
                object-fit: cover;
                border-radius: 3px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            }
            </style>
        """, unsafe_allow_html=True)

        for b in range(0, len(vid_keys), 3):
            col1, col2, col3= st.columns([3, 3, 3])
            with col1:
                if b < len(vid_keys):
                    st.video(vid_dct[vid_keys[b]])
                    st.write(vid_keys[b])
                    # a+1 para enganar o streamlit id do botao
                    if st.button(f"Detalhes", key = f"{vid_keys[b]}"):
                        view_count = 0
                        description_txt = ("Este vídeo curto oferece uma experiência visual envolvente, e estão sujeitos "
                                       "a direitos de autor ideal para demonstrações, testes de streaming ou aplicações "
                                       "educacionais. Hospedado em um servidor Flask, o conteúdo é entregue de forma "
                                       "eficiente e pode ser acessado diretamente via navegador.")
                        st.write(description_txt)
                        st.write(f"Duração minima: {5} min")

                    else:
                        pass

            with col2:
                if b + 1 < len(vid_keys):
                    st.video(vid_dct[vid_keys[b + 1]])
                    st.write(vid_keys[b + 1])
                    # a+2 para enganar o streamlit id do botao
                    if st.button(f"Detalhes", key = f"{vid_keys[b + 1]}"):
                        description_txt = ("Este vídeo curto oferece uma experiência visual envolvente, e estão sujeitos "
                            "a direitos de autor ideal para demonstrações, testes de streaming ou aplicações "
                            "educacionais. Hospedado em um servidor Flask, o conteúdo é entregue de forma "
                            "eficiente e pode ser acessado diretamente via navegador.")
                        st.write(description_txt)
                        st.write(f"Duração minima: {5} min")
                    else:
                        pass

            with col3:
                if b + 2 < len(vid_keys):
                    st.video(vid_dct[vid_keys[b + 2]])
                    st.write(vid_keys[b + 2])
                    # b+10 para enganar o streamlit id do botao
                    if st.button(f"Detalhes", key = f"{vid_keys[b + 2]}"):
                        view_count = 0
                        description_txt = ("Este vídeo curto oferece uma experiência visual envolvente, e estão sujeitos "
                            "a direitos de autor ideal para demonstrações, testes de streaming ou aplicações "
                            "educacionais. Hospedado em um servidor Flask, o conteúdo é entregue de forma "
                            "eficiente e pode ser acessado diretamente via navegador.")
                        st.write(description_txt)
                        st.write(f"Duração minima: {5} min")
                    else:
                        pass
            # quebra de linha 3 a 3 entra as culonas
            st.subheader(" ", divider="gray")
            a += 2

#logotipo unico da pagina
st.image("images/logo_ualflix.png", width=100)

#titulo da pagina
st.title("Ualflix- Sistema de Streaming")
st.title("                               ")


pg2_run = PaginaDois().layout_columns()
