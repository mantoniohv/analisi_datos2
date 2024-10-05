import streamlit as st
import pandas as pd
import plotly.express as px

# Leer el archivo CSV
df = pd.read_csv('C:/Users/manto/proyecto2/vehicles_us.csv')

# Crear un encabezado
st.header("Análisis Exploratorio de Datos con Streamlit")

# Crear el botón para el histograma
hist_button = st.button('Construir histograma')

if hist_button:  # Al hacer clic en el botón
    st.write('Creación de un histograma para el conjunto de datos')
    
    # Crear un histograma utilizando una columna válida, por ejemplo 'odometer'
    fig = px.histogram(df, x="odometer", title="Histograma del Kilometraje (odometer)")
    
    # Mostrar el gráfico de histograma
    st.plotly_chart(fig, use_container_width=True)

# Crear otro botón para el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:  # Al hacer clic en el botón
    st.write('Creación de un gráfico de dispersión para el conjunto de datos')
    
    # Crear un gráfico de dispersión usando las columnas 'price' y 'model_year'
    fig = px.scatter(df, x="model_year", y="price", title="Gráfico de Dispersión entre Año y Precio")
    
    # Mostrar el gráfico de dispersión
    st.plotly_chart(fig, use_container_width=True)


