# Usamos a imagem oficial do Python como base
FROM python:3.10-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /workspace

# Instala dependências do sistema (se necessário) e o cliente do PostgreSQL
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*
