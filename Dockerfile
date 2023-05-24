# Setando slim-booster (mais leve pra uso em cluster)
FROM python:3.11-slim-buster 
WORKDIR /app

# Copiando requerimentos pra raiz
COPY requirements.txt .

# Atualizando e praparando maquina
RUN apt-get update && apt-get install --no-install-recommends --no-install-suggests -y \
    && pip install --no-cache-dir -r requirements.txt 
# Shell
CMD ["bash"]
