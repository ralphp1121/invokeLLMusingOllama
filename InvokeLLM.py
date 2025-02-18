import argparse
from langchain_ollama import OllamaLLM
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

def query_ollama(prompt, model):
    """p
    Send a prompt to local Ollama instance using LangChain and get the response.
    
    Args:
        prompt (str): The prompt to send to the model
        model (str): The model to use (default: llama2)
    
    Returns:
        str: The model's response
    """
    try:
        # Initialize Ollama with streaming callback
        llm = OllamaLLM(
            model=model,
            callbacks=[StreamingStdOutCallbackHandler()],
            # You can add additional parameters here:
            # temperature=0.7,
            # top_p=0.9,
            # num_ctx=4096,
        )
        
        # Generate response using invoke
        response = llm.invoke(prompt)
        return response
        
    except Exception as e:
        return f"Error communicating with Ollama: {str(e)}"

def main():
    parser = argparse.ArgumentParser(description="Send a prompt to local Ollama instance using LangChain and get the response.")
    parser.add_argument("prompt", type=str, help="The prompt to send to the model")
    parser.add_argument("--model", type=str, default="llama3.1", help="The model to use (default: llama3.1)")
    
    args = parser.parse_args()
    
    prompt = args.prompt
    model = args.model
    
    print(f"\nSending prompt to {model}: {prompt}\n")
    print("\nResponse:")
    response = query_ollama(prompt, model)
    
    # Since we're using streaming callback, the response has already been printed
    # You can still use the returned response for other purposes
    print("\nComplete response stored in variable:", response)

if __name__ == "__main__":
    main()