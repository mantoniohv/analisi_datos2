import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Leer el archivo CSV
df = pd.read_csv('data/vehicles_us.csv')

# Crear un encabezado
st.header("Análisis Exploratorio de Datos con Streamlit")

# Crear el botón para el histograma
hist_button = st.button('Construir histograma')

if hist_button:  # Al hacer clic en el botón
    st.write('Creación de un histograma para el conjunto de datos')
    
    # Crear un histograma usando Plotly Graph Objects
    fig = go.Figure(data=[go.Histogram(x=df['odometer'])])
    
    # Mostrar el gráfico de histograma
    st.plotly_chart(fig, use_container_width=True)

# Crear otro botón para el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:  # Al hacer clic en el botón
    st.write('Creación de un gráfico de dispersión para el conjunto de datos')
    
    # Crear un gráfico de dispersión usando Plotly Graph Objects
    fig = go.Figure(data=go.Scatter(x=df['model_year'], y=df['price'], mode='markers'))
    
    # Mostrar el gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True)
