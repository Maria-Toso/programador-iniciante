import streamlit as st
import pandas as pd
import plotly.express as px
from pymongo import MongoClient
import time

st.set_page_config(page_title="Pulse-Sentinel Dashboard", layout="wide")
st.title("⚡ Pulse-Sentinel: Real-Time Web Sentiment")

# Conexão com o MongoDB Atlas via Secrets
# Certifique-se de salvar MONGO_URI nos Secrets do Streamlit!
@st.cache_resource
def init_connection():
    return MongoClient(st.secrets["MONGO_URI"])

client = init_connection()
db = client['PulseSentinel'] # Nome do banco que você criou no Atlas
collection = db['sentiments']

placeholder = st.empty()

while True:
    try:
        # Busca os últimos 100 documentos do MongoDB
        data = list(collection.find().sort("_id", -1).limit(100))
        
        if not data:
            st.warning("Banco de dados vazio. Ligue o Ingestor e o Processador!")
            time.sleep(5)
            continue

        df = pd.DataFrame(data)
        
        # Processamento dos dados para o Dashboard
        total = len(df)
        counts = df['label'].value_counts().to_dict()
        pos = counts.get('LABEL_2', 0) # Ajuste o label conforme sua IA
        neg = counts.get('LABEL_0', 0)

        with placeholder.container():
            kpi1, kpi2, kpi3 = st.columns(3)
            kpi1.metric("Total Analisado (Sessão)", total)
            kpi2.metric("Positivos 👍", pos)
            kpi3.metric("Negativos 👎", neg)

            fig = px.pie(
                values=[pos, neg, counts.get('LABEL_1', 0)], 
                names=['Positivo', 'Negativo', 'Neutro'],
                hole=0.4,
                title="Distribuição de Sentimento Real-Time"
            )
            st.plotly_chart(fig, use_container_width=True)

            st.write("### Últimos Insights do MongoDB Atlas")
            st.dataframe(df[['content', 'label', 'score']].head(10))

        time.sleep(5) # Aumentei para 5s para não fritar o free tier do Atlas
    except Exception as e:
        st.error(f"Erro ao conectar no MongoDB Atlas: {e}")
        time.sleep(10)
