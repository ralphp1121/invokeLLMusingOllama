# Using Python to Interact with Local Ollama LLM

This guide demonstrates how to use Python to interact with a locally installed Ollama LLM instance on a MacBook. The implementation uses the `langchain-ollama` package to facilitate communication with the Ollama service.

## Prerequisites

Before running the code, ensure you have:

1. Python 3.x installed on your MacBook
2. Ollama installed and running locally
3. At least one LLM model downloaded via Ollama (e.g., llama2)
4. A Python virtual environment set up

## Setup Instructions

### Create and Activate Virtual Environment

```bash
# Create a new directory for your project
mkdir ollama_project
cd ollama_project

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate
```

### Install Required Packages

```bash
pip install langchain langchain-ollama
```

## Code Implementation

The implementation consists of two main parts:

### 1. Imports and Dependencies

```python
from langchain_ollama import OllamaLLM
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
```

Key components:
- `OllamaLLM`: Main class for interacting with Ollama
- `StreamingStdOutCallbackHandler`: Enables real-time streaming of LLM responses

### 2. Main Function Implementation

```python
def query_ollama(prompt, model="llama2"):
    try:
        # Initialize Ollama with streaming callback
        llm = OllamaLLM(
            model=model,
            callbacks=[StreamingStdOutCallbackHandler()],
        )
        
        # Generate response using invoke
        response = llm.invoke(prompt)
        return response
        
    except Exception as e:
        return f"Error communicating with Ollama: {str(e)}"
```

Key features:
- **Default Model**: Uses "llama2" as the default model
- **Streaming Output**: Implements real-time response streaming
- **Error Handling**: Includes basic error handling for API communication
- **Invoke Method**: Uses the modern `invoke()` method instead of deprecated call syntax

## Usage Example

```python
def main():
    prompt = "Explain what is quantum computing in simple terms."
    model = "llama2"
    
    print(f"\nSending prompt to {model}: {prompt}\n")
    print("\nResponse:")
    response = query_ollama(prompt, model)
    print("\nComplete response stored in variable:", response)

if __name__ == "__main__":
    main()
```

## Optional Configuration

The `OllamaLLM` class supports various configuration parameters:

```python
llm = OllamaLLM(
    model=model,
    callbacks=[StreamingStdOutCallbackHandler()],
    temperature=0.7,    # Controls randomness (0.0 to 1.0)
    top_p=0.9,         # Nucleus sampling parameter
    num_ctx=4096,      # Context window size
)
```

## Common Issues and Solutions

1. **Import Error**: If you see `ImportError: cannot import name 'OllamaLLM'`, ensure you have installed `langchain-ollama` package.

2. **Connection Error**: If you can't connect to Ollama, verify:
   - Ollama service is running (`ollama serve`)
   - The desired model is downloaded (`ollama pull model_name`)
   - No firewall is blocking the connection

3. **Virtual Environment**: Always ensure your virtual environment is activated before running the code:
   ```bash
   source venv/bin/activate
   ```

## Best Practices

1. Always use a virtual environment to manage dependencies
2. Include proper error handling in production code
3. Use streaming callbacks for better user experience with long responses
4. Keep the Ollama service running while making API calls
5. Monitor system resources when running large language models locally

## Additional Resources

- [Ollama Documentation](https://ollama.ai/docs)
- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction)
- [LangChain-Ollama Package](https://python.langchain.com/docs/integrations/llms/ollama)