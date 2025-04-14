FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV USE_MODEL=openai
ENV OLLAMA_BASE=http://host.docker.internal:11434
CMD ["python", "run.py"]