import streamlit as st
import math

# título
st.title("Calculadora de IMC")

# subtítulo
st.markdown("Este é um Aplicativo utilizado para calcular o seu IMC")

altura = st.slider('Insira sua altura em centímetros', 50, 250)

peso = st.number_input(label='Informe seu Peso (em Quilos)', min_value=0.0, 
                    max_value=200.0, value=70.0, step=0.5, format=None, key=None)           


imc = peso / math.pow((altura/100), 2)

st.write('Seu IMC é de: ', round(imc, 1))

if imc < 18.5:
    st.write('Resultado: Você está abaixo do peso ideal')
elif imc < 25:
    st.write('Resultado: Você está dentro do peso')
else:
    st.write('Resultado: Você está acima do peso')    