import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("vehicles_us.csv")

st.header("Dashboard de Anuncios de Coches")
st.write("Visualiza histogramas y gráficos de dispersión de los anuncios de coches.")


hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Histograma de kilometraje de los coches')
    fig = px.histogram(df, x="odometer", nbins=30, title="Kilometraje de vehículos")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Gráfico de dispersión: Precio vs Año por fabricante')
    fig2 = px.scatter(df, x="year", y="price", color="manufacturer", title="Precio vs Año")
    st.plotly_chart(fig2, use_container_width=True)
