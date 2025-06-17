# Use an official Python image
FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y curl git && \
    apt-get clean

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Install Python dependencies
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Download the model ahead of time (optional)
RUN ollama pull llama3.2

# Expose Railway's default port
ENV PORT 8080
EXPOSE 8080

# Run Ollama in background + Streamlit
CMD bash -c "ollama serve & streamlit run app.py --server.port 8080 --server.address 0.0.0.0"
