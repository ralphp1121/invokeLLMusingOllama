# Ollama LLM Python Integration

This repository contains a Python application that interacts with a locally running Ollama LLM instance. The implementation leverages LangChain to facilitate communication with Ollama and provides a straightforward command-line interface for generating LLM responses.

## Overview

The application allows you to:
- Send prompts to any LLM model available in your Ollama installation
- Receive real-time streaming responses
- Configure which model to use via command-line arguments

## Prerequisites

- Python 3.x
- Ollama installed and running
- At least one LLM model downloaded in Ollama (e.g., llama3.1, llama2)

## Installation

### Direct Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ralphp1121/invokeLLMusingOllama.git
   cd invokeLLMusingOllama
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:
   ```bash
   pip install langchain langchain-ollama
   ```

### Docker Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ralphp1121/invokeLLMusingOllama.git
   cd invokeLLMusingOllama
   ```

2. Build the Docker image:
   ```bash
   docker build -t ollama-llm-exec .
   ```

3. Run the Docker container:
   ```bash
   docker run -d --name ollama-container ollama-llm-exec
   ```

   The container automatically:
   - Starts the Ollama service
   - Downloads default models (llama3.1 and llama2)
   - Remains running, waiting for commands

## Usage

### Command-Line Arguments

The application accepts the following command-line arguments:

| Argument | Description | Required | Default |
|----------|-------------|----------|---------|
| `prompt` | The text prompt to send to the LLM | Yes | N/A |
| `--model` | The Ollama model to use | No | llama3.1 |

### Local Usage

If you've installed the application directly on your machine:

```bash
python InvokeLLM.py "Your prompt here" --model llama3.1
```

Examples:
```bash
# Use default model (llama3.1)
python InvokeLLM.py "Explain how photosynthesis works"

# Specify a different model
python InvokeLLM.py "Write a short poem about the moon" --model llama2
```

### Docker Usage

If you're using the Docker installation:

```bash
docker exec ollama-container python3 /app/InvokeLLM.py "Your prompt here" --model llama3.1
```

Examples:
```bash
# Use default model (llama3.1)
docker exec ollama-container python3 /app/InvokeLLM.py "What is quantum computing?"

# Specify a different model
docker exec ollama-container python3 /app/InvokeLLM.py "Write a haiku about spring" --model llama2
```

## Working with Docker Container

### Check Container Status
```bash
docker logs ollama-container
```

### Pull Additional Models
```bash
docker exec ollama-container ollama pull mistral
```

### List Available Models
```bash
docker exec ollama-container ollama list
```

### Stop the Container
```bash
docker stop ollama-container
```

### Restart the Container
```bash
docker start ollama-container
```

## Code Structure

The Python code consists of two main functions:

1. `query_ollama(prompt, model)`:
   - Initializes the OllamaLLM instance
   - Configures streaming callbacks
   - Handles errors during the API call
   - Returns the LLM's response

2. `main()`:
   - Parses command-line arguments
   - Calls the `query_ollama` function
   - Displays the response

## Customization

You can customize the LLM parameters by modifying the initialization options:

```python
llm = OllamaLLM(
    model=model,
    callbacks=[StreamingStdOutCallbackHandler()],
    temperature=0.7,    # Controls randomness (0.0 to 1.0)
    top_p=0.9,         # Nucleus sampling parameter
    num_ctx=4096,      # Context window size
)
```

## Troubleshooting

1. **Ollama Service Not Running**:
   - Ensure Ollama is installed and running with `ollama serve`

2. **Model Not Found**:
   - Download the model first with `ollama pull <model_name>`

3. **Import Errors**:
   - Verify you've installed the required packages with `pip install langchain langchain-ollama`

4. **Docker Network Issues**:
   - If using Docker, ensure you have proper network connectivity

## License

[Include your license information here]

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.