import secrets
import string
import streamlit as st
from wonderwords import RandomWord

# Título do aplicativo na web
st.title("Gerador de Senhas Seguras")
st.write(
    "Use os campos abaixo para definir como você quer a sua senha personalizada:"
)

# Campos de entrada na tela (substituindo os input() antigos)
decisão_palavras = st.number_input(
    "1. Quantidade de palavras na senha", min_value=1, max_value=10, value=3
)
decisão_números = st.number_input(
    "2. Quantidade de números na senha", min_value=0, max_value=10, value=2
)
decisão_simbolos = st.number_input(
    "3. Quantidade de símbolos na senha", min_value=0, max_value=10, value=1
)

# Botão para gerar a senha
if st.button("Gerar Senha"):
  rw = RandomWord()
  senha_lista = []
  números = ""

  for i in range(int(decisão_palavras)):
    choicer = rw.word().capitalize()
    senha_lista.append(choicer)

  simbolo = secrets.choice(string.punctuation)
  palavras_juntas = simbolo.join(senha_lista)

  for i in range(int(decisão_números)):
    números += secrets.choice(string.digits)

  simbolos_extras = ""
  for i in range(int(decisão_simbolos)):
    simbolos_extras += secrets.choice(string.punctuation)

  senha_pronta = palavras_juntas + números + simbolos_extras

  # 4. Resultado exibido na tela
  st.success("4. Resultado da Senha:")
  st.code(senha_pronta, language="")