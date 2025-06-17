FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y curl git && \
    apt-get clean

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy your app code
COPY . .

# Expose port for Streamlit
EXPOSE 8080
ENV PORT=8080

# Start Ollama, pull model, then run Streamlit
CMD bash -c "ollama serve & sleep 5 && ollama pull llama3.2 && streamlit run app.py --server.port 8080 --server.address 0.0.0.0"
