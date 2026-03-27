FROM python:3.11-bullseye

RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    apt-transport-https \
    unixodbc-dev \
    && rm -rf /var/lib/apt/lists/*

RUN wget -qO- https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN wget -q https://packages.microsoft.com/config/debian/11/prod.list \
    -O /etc/apt/sources.list.d/mssql-release.list

RUN apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql18 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD ["python", "app.py"]