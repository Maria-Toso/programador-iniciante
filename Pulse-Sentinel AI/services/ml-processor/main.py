import json
from kafka import KafkaConsumer
from pymongo import MongoClient
from transformers import pipeline

# Configurações
KAFKA_SERVER = 'localhost:9092'
MONGO_URI = 'mongodb://localhost:27017/'
TOPIC_RAW = 'raw_tweets'

# Inicializa o MongoDB 
client = MongoClient(MONGO_URI)
db = client['pulse_db']
collection = db['sentiments']

# Inicializa o modelo de IA
# Na primeira execução, ele vai baixar uns 500MB.
print("🧠 Carregando modelo RoBERTa... Vai buscar um café.")
analyzer = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")

# Inicializa o Consumer do Kafka
consumer = KafkaConsumer(
    TOPIC_RAW,
    bootstrap_servers=[KAFKA_SERVER],
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    auto_offset_reset='earliest'
)

def process_sentiment(text):
    # O modelo retorna LABEL_0 (neg), LABEL_1 (neu), LABEL_2 (pos)
    result = analyzer(text[:512])[0] # Tem limite de 512 tokens
    return result

if __name__ == "__main__":
    print("🚀 Processador de IA ativo. Analisando a toxicidade da internet...")
    
    for message in consumer:
        data = message.value
        sentiment = process_sentiment(data['content'])
        
        # Enriquece o dado original com a análise da IA
        enriched_data = {
            **data,
            "label": sentiment['label'],
            "score": sentiment['score'],
            "processed_at": time.time()
        }
        
        # Salva no Mongo
        collection.insert_one(enriched_data)
        print(f" [✅] Processado: {sentiment['label']} ({sentiment['score']:.2f})")
