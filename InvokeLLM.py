from langchain_community.llms import OllamaLLM
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

def query_ollama(prompt, model="llama3.1"):
    """
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
    # Example prompt - you can modify this
    prompt = "Explain what is quantum computing in simple terms like I'm 5 years old."
    
    # You can change the model to any model you have pulled in Ollama
    model = "llama3.1"
    
    print(f"\nSending prompt to {model}: {prompt}\n")
    print("\nResponse:")
    response = query_ollama(prompt, model)
    
    # Since we're using streaming callback, the response has already been printed
    # You can still use the returned response for other purposes
    print("\nComplete response stored in variable:", response)

if __name__ == "__main__":
    main()