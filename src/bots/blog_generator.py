from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
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
    messages = [
        SystemMessage(content=prompts.blog_prompt),
        HumanMessage(content=str(nl_text))
    ]
    
    return [chunk for chunk in model.stream(messages)]

def generate_metadata(blog_output: str) -> str:
    """
    Generates metadata for blog based on initial blog output.
    
    Args:
        blog_output (str): Generated blog content
        
    Returns:
        str: Generated metadata
    """
    model = ChatOpenAI(model=BOT_REMOTE, temperature=0)
    messages = [
        SystemMessage(content=prompts.metadata_prompt),
        HumanMessage(content=str(blog_output))
    ]
    
    return [chunk for chunk in model.stream(messages)]