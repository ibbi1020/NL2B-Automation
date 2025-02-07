from langchain_ollama import ChatOllama 
from langchain.globals import set_debug
from langchain.output_parsers import StructuredOutputParser

#set_debug(True)

def generate_blog(newsletter_text):
    
    """Generates a blog from the given newsletter text"""
    model = OllamaLLM(model ="deepseek-r1:8b", temperature = 0)
    prompt = f"""
    <<<Convert the following newsletter into a well-structured blog post while maintaining the original intent and improving readability>>>:
    
    {newsletter_text}

    """
    
    response = model.invoke(prompt)
    return response