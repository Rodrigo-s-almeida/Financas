import streamlit as st
import math
from PIL import Image
import requests

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
elif imc < 24.9:
    st.write('Resultado: Você está no peso ideal (Parabéns)')    
elif imc < 29.9:
    st.write('Resultado: Você está levemente acima do peso')
elif imc < 34.9:
    st.write('Resultado: Obesidade Grau I')
elif imc < 39.9:
    st.write('Resultado: Obesidade Grau II (SEVERA)')
else:
    st.write('Resultado: Obesidade Grau III (MÓRBIDA)')   

im_magro = Image.open(requests.get('https://raw.githubusercontent.com/Rodrigo-s-almeida/Financas/main/emoji_magro.jpg', stream=True).raw)
im_ideal = Image.open(requests.get('https://raw.githubusercontent.com/Rodrigo-s-almeida/Financas/main/emoji_ideal.jpg', stream=True).raw)   
im_levemente = Image.open(requests.get('https://raw.githubusercontent.com/Rodrigo-s-almeida/Financas/main/emoji_levemente.jpg', stream=True).raw)
im_grau1 = Image.open(requests.get('https://raw.githubusercontent.com/Rodrigo-s-almeida/Financas/main/emoji_grau1.jpg', stream=True).raw)
im_grau2 = Image.open(requests.get('https://raw.githubusercontent.com/Rodrigo-s-almeida/Financas/main/emoji_grau2.jpg', stream=True).raw)
im_grau3 = Image.open(requests.get('https://raw.githubusercontent.com/Rodrigo-s-almeida/Financas/main/emoji_grau3.jpg', stream=True).raw)


if imc < 18.5:
    st.image(im_magro)
elif imc < 24.9:
    st.image(im_ideal)
elif imc < 29.9:
    st.image(im_levemente)
elif imc < 34.9:
    st.image(im_grau1)
elif imc < 39.9:
    st.image(im_grau2)   
else:
    st.image(im_grau3) 
