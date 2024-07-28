FROM python:3.8-slim

# Instalar dependências necessárias para Gedit e Firefox
RUN apt-get update && apt-get install -y --no-install-recommends \
    gedit \
    firefox-esr \
    x11-apps \
    && rm -rf /var/lib/apt/lists/*

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos de requisitos para o contêiner
COPY requirements.txt .

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante dos arquivos da aplicação para o contêiner
COPY . .

# Configurar a variável DISPLAY
ENV DISPLAY=:0

# Comando para iniciar a aplicação Flask, Gedit e abrir o Firefox no endereço da aplicação
CMD python app.py & firefox http://localhost:5000
