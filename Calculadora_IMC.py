import streamlit as st
import math
from PIL import Image

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

#im_magro = Image.open('C:/Python/Streamlit/magro.jpg')    
#im_normal = Image.open('C:/Python/Streamlit/emoji_legal.jpg')    
#im_gordo = Image.open('C:/Python/Streamlit/emoji_polegar_para_baixo.jpg')    


im_magro = Image.open('https://github.com/Rodrigo-s-almeida/Financas/main/magro.jpg')    
im_normal = Image.open('https://github.com/Rodrigo-s-almeida/Financas/main/emoji_legal.jpg')    
im_gordo = Image.open('https://github.com/Rodrigo-s-almeida/Financas/main/emoji_polegar_para_baixo.jpg') 


if imc < 18.5:
    st.image(im_magro)
elif imc < 25:
    st.image(im_normal)
else:
    st.image(im_gordo) 
