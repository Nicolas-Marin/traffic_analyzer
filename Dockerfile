FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
COPY traffic_analyzer.py .
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y tcpdump && rm -rf /var/lib/apt/lists/*
CMD ["python", "traffic_analyzer.py"]
