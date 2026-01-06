# ⚡ Pulse-Sentinel AI 

> **Real-time Emotional Intelligence at Scale.**

[![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)](https://python.org)
[![Kafka](https://img.shields.io/badge/Apache_Kafka-Data_Stream-black?style=for-the-badge&logo=apachekafka)](https://kafka.apache.org/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-blue?style=for-the-badge&logo=docker)](https://docker.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

## 🧠 O Conceito

O **Pulse-Sentinel** não é apenas mais um "sentiment analysis" básico que encontras em tutoriais de iniciantes. É um motor de processamento de eventos distribuído, desenhado para ingerir, processar e visualizar o estado emocional da internet em tempo real. 

Se o mundo está a entrar em colapso no X (Twitter) ou se o Reddit decidiu inflacionar uma ação da GameStop, o Pulse-Sentinel deteta a mudança de paradigma antes de o primeiro jornalista acordar.

## 🛠️ Tech Stack (The "No-BS" Architecture)

- **Engine:** Python 3.11 com `asyncio` para máxima concorrência.
- **Data Pipeline:** `Apache Kafka` atuando como a espinha dorsal para streaming de dados massivos.
- **AI/NLP Layer:** Modelos `RoBERTa` (via Hugging Face) otimizados para deteção de sarcasmo e toxicidade.
- **Storage:** `MongoDB` para os dados brutos e `Redis` para cache de milissegundos.
- **Frontend:** `Next.js 14` com WebSockets para atualizações que não precisam de refresh.
- **Ops:** `Docker` & `GitHub Actions` (CI/CD).

## 🚀 Como Correr Esta Besta

### Pré-requisitos
- Docker & Docker Compose (Se não tens isto, o que estás a fazer com a tua vida?)
- API Keys (X, Reddit ou NewsAPI)

### Setup Rápido
1. Clona o repo: `git clone https://github.com/teu-user/pulse-sentinel.git`
2. Configura o `.env` (não sejas nabo, não dês commit nas tuas chaves).
3. Levanta a infraestrutura:
   ```bash
   docker-compose up -d
