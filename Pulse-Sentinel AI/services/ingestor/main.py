import json
import time
import requests
from kafka import KafkaProducer

# Configurações básicas (Pega tua key no newsapi.org)
API_KEY = 'SUA_KEY_AQUI'
TOPIC_NAME = 'raw_tweets'
KAFKA_SERVER = 'localhost:9092'

# Inicializa o Producer do Kafka
# O value_serializer garante que a gente envie JSON
producer = KafkaProducer(
    bootstrap_servers=[KAFKA_SERVER],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

def fetch_news(query="crypto"):
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        for art in articles:
            payload = {
                "source": art['source']['name'],
                "content": art['title'] + " " + (art['description'] or ""),
                "timestamp": art['publishedAt']
            }
            # Joga na fila do Kafka para o processador de IA pegar depois
            producer.send(TOPIC_NAME, value=payload)
            print(f" [🔥] Enviado para o Kafka: {art['title'][:50]}...")
    else:
        print(f" [❌] Erro na API: {response.status_code}")

if __name__ == "__main__":
    print("🚀 Ingestor iniciado. Monitorando o caos...")
    while True:
        fetch_news("tecnologia")
        time.sleep(60) # Pra não banirem seu IP em 2 minutos
