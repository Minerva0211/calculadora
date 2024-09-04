# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PIwkOBxi7FRyXHAcXE9bAA2M5U7faIai
"""

import streamlit as st
import numpy as np
import plotly.express as px

# Título de la app
st.title("Calculadora de Predicción de Gastos")

# Sección para ingresar los datos
st.header("Ingresa los datos:")
mes = st.number_input("Mes del año", min_value=1, max_value=12, step=1)
venta_mensual_vehiculo = st.number_input("venta mensual x vehículo", min_value=0.0, step=100.0)
combustible_mensual = st.number_input("combustible mensual", min_value=0.0, step=50.0)
impacto_combustible = st.number_input("impacto del combustible", min_value=0.0, step=0.1)
venta_mensual_total = st.number_input("venta mensual", min_value=0.0, step=1000.0)

# Botón para generar la predicción
if st.button("Generar Pronóstico"):

    # Función que realiza la predicción basada en los coeficientes
    def calcular_prediccion(venta_mensual_vehiculo, combustible_mensual, impacto_combustible, venta_mensual_total):
        """

        Args:
          venta_mensual_vehiculo:
          combustible_mensual:
          impacto_combustible:
          venta_mensual_total:

        Returns:

        """
        # Coeficientes de la fórmula
        b0 = 1000  # Intercepto (puedes ajustarlo)
        b1 = 0.476   # Coeficiente para venta_mensual_vehiculo
        b2 = 0.000  # Coeficiente para combustible_mensual
        b3 = 0.280  # Coeficiente para impacto_combustible
        b4 = 0.032
        b5 = 0.000 # Coeficiente para venta_mensual_total

        # Fórmula de predicción
        prediccion = b0 + (b1 * venta_mensual_x_vehículo) + (b2 * combustible_mensual) + (b3 * impacto_combustible) + (b4 * venta_mensual_total)
        return prediccion

    # Realizar el cálculo
    resultado = calcular_prediccion(venta_mensual_x_vehículo, combustible_mensual, impacto_combustible, venta_mensual_total)

    # Mostrar el resultado de la predicción
    st.subheader(f"El pronóstico de gasto de mantenimiento por vehiculo es: ${resultado:,.2f}")

    # Visualización gráfica
    datos = {
        'Variables': ['Mes''Venta Vehículo', 'Combustible', 'Impacto Combustible', 'Venta Total'],
        'Valores': [mes, venta_mensual_x_vehículo, combustible_mensual, impacto_combustible, venta_mensual_total]
    }

    fig = px.bar(datos, x='Variables', y='Valores', title="Datos Ingresados para el Pronóstico")
    st.plotly_chart(fig)

# Pie de página
st.write("Esta app es un ejemplo de cómo generar pronósticos basados en coeficientes con Streamlit.")

