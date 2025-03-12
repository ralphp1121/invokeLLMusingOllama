# Use Ubuntu as base image
FROM ubuntu:22.04

# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    python3 \
    python3-pip \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

# Install Ollama
RUN curl -L https://ollama.ai/install.sh | bash

# Create app directory
WORKDIR /app

# Clone the repository
RUN git clone https://github.com/ralphp1121/invokeLLMusingOllama.git /app

# Create and activate virtual environment
RUN python3 -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

# Install Python dependencies
RUN pip3 install --no-cache-dir \
    langchain \
    langchain-ollama \
    argparse

# Create a startup script that just starts Ollama service
RUN echo '#!/bin/bash\n\
echo "Starting Ollama service..."\n\
ollama serve &\n\
sleep 3\n\
echo "Pulling default models (llama3.1 and llama2)..."\n\
ollama pull llama3.1\n\
ollama pull llama2\n\
echo "Ollama service is ready to use!"\n\
echo "Run your Python script with: docker exec <container_id> python3 /app/InvokeLLM.py \"Your prompt here\" --model llama3.1"\n\
# Keep the container running\n\
tail -f /dev/null\n\
' > /app/start.sh

# Make the startup script executable
RUN chmod +x /app/start.sh

# Set the startup script as the entry point
ENTRYPOINT ["/app/start.sh"]