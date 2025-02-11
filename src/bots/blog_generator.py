from langchain_openai import ChatOpenAI
from ..config.settings import BOT_REMOTE
import prompts

def generate_blog(nl_text: str) -> list:
    """
    Generates a blog from the given newsletter text.
    
    Args:
        nl_text (str): Newsletter text input
        
    Returns:
        list: Generated blog content chunks
    """
    model = ChatOpenAI(model=BOT_REMOTE, temperature=0)
    prompt = prompts.blog_prompt.format(newsletter_text=nl_text)
    
    return [chunk for chunk in model.stream(prompt)]

def generate_metadata(blog_output: str) -> str:
    """
    Generates metadata for blog based on initial blog output.
    
    Args:
        blog_output (str): Generated blog content
        
    Returns:
        str: Generated metadata
    """
    model = ChatOpenAI(model=BOT_REMOTE, temperature=0)
    prompt = prompts.metadata_prompt.format(blog_output=blog_output)
    
    return model.invoke(prompt)