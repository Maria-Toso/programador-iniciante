from fastapi import FastAPI
from pymongo import MongoClient
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Pulse-Sentinel API")

# Permitir que o Frontend acesse a API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = MongoClient('mongodb://localhost:27017/')
db = client['pulse_db']

@app.get("/stats")
def get_stats():
    col = db['sentiments']
    # Pega os últimos 100 registros para o dashboard
    data = list(col.find({}, {'_id': 0}).sort("processed_at", -1).limit(100))
    
    # Faz um resumão rápido
    total = len(data)
    pos = len([d for d in data if d['label'] == 'LABEL_2'])
    neg = len([d for d in data if d['label'] == 'LABEL_0'])
    
    return {
        "total_analyzed": total,
        "sentiment_breakdown": {
            "positive": pos,
            "negative": neg,
            "neutral": total - (pos + neg)
        },
        "recent_data": data
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
