import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import time

st.set_page_config(page_title="Pulse-Sentinel Dashboard", layout="wide")

st.title("⚡ Pulse-Sentinel: Real-Time Web Sentiment")

# Placeholder para o dashboard atualizar em tempo real
placeholder = st.empty()

while True:
    try:
        response = requests.get("http://localhost:8000/stats").json()
        df = pd.DataFrame(response['recent_data'])

        with placeholder.container():
            # Métricas principais
            kpi1, kpi2, kpi3 = st.columns(3)
            kpi1.metric("Total Analisado", response['total_analyzed'])
            kpi2.metric("Positivos 👍", response['sentiment_breakdown']['positive'])
            kpi3.metric("Negativos 👎", response['sentiment_breakdown']['negative'])

            # Gráfico de Rosca (Donut Chart)
            fig = px.pie(
                values=list(response['sentiment_breakdown'].values()), 
                names=list(response['sentiment_breakdown'].keys()),
                hole=0.4,
                title="Distribuição de Sentimento"
            )
            st.plotly_chart(fig, use_container_width=True)

            # Tabela de dados brutos
            st.write("### Últimos Insights Processados")
            st.dataframe(df[['content', 'label', 'score']].head(10))

        time.sleep(2) # Refresh a cada 2 segundos
    except Exception as e:
        st.error(f"Esperando API ou Kafka... {e}")
        time.sleep(5)
