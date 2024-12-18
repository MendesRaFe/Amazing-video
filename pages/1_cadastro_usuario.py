import streamlit as st
from estruturas import Usuario
from service import SistemaRecomendacao

sistema = SistemaRecomendacao(SistemaRecomendacao.dirOntos())
usuario1 = Usuario()

st.title("Cadastro")

st.write("### Novo Usuário")

col11, col12 = st.columns(2)

usuario1.nome = col11.text_input("Nome", "")
usuario1.email = col11.text_input("Email", "")
usuario1.idade = col12.number_input("Idade", min_value=0, max_value=130)
usuario1.telefone = col12.text_input("Telefone", "")


st.write("### Novo Usuário")

col21, col22 = st.columns(2)

options = st.multiselect(
    "Escolha os generos de filme que não podem faltar na sua lista?",
    sistema.listar_generos(),
    max_selections=3,
)

left, right = st.columns(2)

# Btn Voltar - Leva de volta à Home
if left.button("Voltar", type='secondary', use_container_width=True):
    st.switch_page("home.py")

# Btn Cadastrar - Invoca a função para cadastrar o novo usuario na base de conhecimento
if right.button("Cadastrar", type='primary', use_container_width=True):
    st.markdown("You clicked the Material button.")