import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sistema EcoTránsito CDMX", layout="wide")
st.title("Sistema EcoTránsito CDMX - Reporte Completo")

# Datos directos
data = {
    'ID_Registro': ['REG-001', 'REG-002', 'REG-003', 'REG-004',
                    'REG-005', 'REG-006', 'REG-007', 'REG-008', 'REG-009', 'REG-010'],
    'Zona_Estacion': ['Centro_Historico', 'Centro_Historico',
                      'Centro_Historico', 'Zona_Oriente', 'Zona_Oriente', 'Zona_Oriente',
                      'Zona_Sur', 'Zona_Sur', 'Zona_Sur', 'Zona_Sur'],
    'Concentracion_PM25': [35.4, 42.1, 38.75, 120.5, 76.45, 32.55, 18.2,
                           20.1, 19.5, 19.5],
    'Nivel_NO2': [42.1, 48.5, 51.0, 89.2, 82.0, 195.0, 22.4, 33.75, 25.1,
                 25.1],
    'Indice_Trafico_Vehicular': [85.0, 92.5, 88.0, 98.0, 91.2, 15.0,
                                 45.0, 42.1, 43.5, 41.0]
}
df = pd.DataFrame(data)

# Métricas (KPIs)
st.markdown("### Indicadores Principales")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Lecturas Activas", value=len(df))
with col2:
    st.metric(label="Promedio PM₂.₅ (μg/m³)", value=f"{df['Concentracion_PM25'].mean():.2f}")
with col3:
    st.metric(label="Máximo Tráfico Vehicular", value=f"{df['Indice_Trafico_Vehicular'].max():.1f}")

st.divider()

# Gráfica 1
st.subheader("1. Relación entre Tráfico Vehicular y Concentración de PM2.5")
fig1 = px.scatter(
    df,
    x="Indice_Trafico_Vehicular",
    y="Concentracion_PM25",
    color="Zona_Estacion",
    labels={"Indice_Trafico_Vehicular": "Índice de Tráfico", "Concentracion_PM25": "PM2.5 (μg/m³)"}
)
st.plotly_chart(fig1, use_container_width=True)

st.divider()

# Gráfica 2
st.subheader("2. Matriz de Correlación de Variables Numéricas")
cols_num = ['Concentracion_PM25', 'Nivel_NO2', 'Indice_Trafico_Vehicular']
fig_sns, ax = plt.subplots(figsize=(6, 4))
sns.heatmap(df[cols_num].corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
st.pyplot(fig_sns)