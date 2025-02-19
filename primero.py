# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 19:46:37 2025


@author: USUARIO
"""
#CMD.exe.Prompt
#(streamlit) C:\Users\USUARIO>cd C:\Users\USUARIO\Desktop\Python_Course\Módulo 10_ Creación de Tableros Dash y aplicaciones Streamlit\clase_streamlit
#(streamlit) C:\Users\USUARIO\Desktop\Python_Course\Módulo 10_ Creación de Tableros Dash y aplicaciones Streamlit\clase_streamlit>streamlit run primero.py
import streamlit as st

st.title('Mi primera página en streamlit')

st.header("Vamos a poner un modelo en producción usando streamlit")

st.subheader("Esto está muy emocionante")

st.text('Esto es un texto')

st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

age = st.slider('How old are you?', 50, 100, 60)
st.write("I'm ", age, 'years old')

st.warning('This is a warning')

st.info("Esto es un info")
st.success('This is a success message!', icon="✅")



