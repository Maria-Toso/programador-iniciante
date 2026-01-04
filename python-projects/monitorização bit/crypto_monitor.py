import requests
import time
from datetime import datetime

# Configurações do seu Alerta
MOEDA = "bitcoin"      # Pode mudar para "ethereum" ou "solana"
BASE_CURRENCY = "usd"  # Moeda de comparação (usd ou eur)
PRECO_ALVO = 65000     # O bot avisa-te se o preço baixar disto

def obter_preco():
    try:
        # URL da API pública da CoinGecko
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={MOEDA}&vs_currencies={BASE_CURRENCY}"
        resposta = requests.get(url)
        dados = resposta.json()
        return dados[MOEDA][BASE_CURRENCY]
    except Exception as e:
        print(f"Erro ao conectar à API: {e}")
        return None

print(f"--- Iniciando Monitor de {MOEDA.upper()} ---")
print(f"Alerta definido para: ${PRECO_ALVO}\n")

while True:
    preco_atual = obter_preco()
    
    if preco_atual:
        agora = datetime.now().strftime("%H:%M:%S")
        
        if preco_atual <= PRECO_ALVO:
            status = "🚨 ALERTA: HORA DE COMPRAR! 🚨"
        else:
            status = "✅ Preço estável"

        print(f"[{agora}] {MOEDA.capitalize()}: ${preco_atual:,.2f} | {status}")
    
    # Espera 30 segundos antes de verificar novamente
    time.sleep(30)
