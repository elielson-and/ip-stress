# Setando slim-booster (mais leve pra uso em cluster)
FROM python:3.11-slim-buster 
WORKDIR /app

# Copiando requerimentos pra raiz
COPY requirements.txt .

# Atualizando e praparando maquina
RUN apt-get update && apt-get install --no-install-recommends --no-install-suggests -y \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get install --no-install-recommends --no-install-suggests -y build-essential \
    && apt-get install --no-install-recommends --no-install-suggests -y libgmp-dev libmpfr-dev libmpc-dev \
    && apt-get install -y wget \
    && make && make install \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Shell
CMD ["bash"]
