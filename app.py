import streamlit as st

st.set_page_config(
    page_title="Minha pagina com jogos", page_icon="🚀", layout="centered"
)
st.write(
    "Bem-vindo ao meu site! Use os botões abaixo para navegar entre os meus"
    " aplicativos."
)
st.markdown(
    """
    <style>
        [data-testid="stSidebarNav"] {display: none;}
        section[data-testid="stSidebar"] {display: none;}
    </style>
""",
    unsafe_allow_html=True,
)

st.info(
    "Clique em um dos botões para testar os projetos que te interessem."
)

st.divider()

# Criação de botões para os seus projetos (substitua pelos nomes reais dos arquivos na pasta pages)
st.subheader("Meus Projetos:")

# Exemplo para o seu gerador de senhas
if st.page_link("pages/gerador de senhas ONLINE.py", label="Gerador de Senhas", icon="🔒"):
    pass

# Exemplo se você tiver outro projeto na pasta pages
# if st.page_link("pages/outro_jogo.py", label="🎮 Abrir Outro Jogo", icon="🎯"):
#     pass
