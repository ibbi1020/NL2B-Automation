from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
import json
from typing import List, Dict
from .utils import render_visuals
from ..config.settings import BOT_REMOTE
import prompts

def generate_visuals(blog_output: str) -> None:
    """
    Identifies placeholders in the blog and generates visualizations.
    
    Args:
        blog_output (str): Generated blog content
    """
    model = ChatOpenAI(model=BOT_REMOTE, temperature=0)
    
    visuals_prompt = PromptTemplate.from_template(prompts.visual_prompt)
    formatted_prompt = visuals_prompt.format(blog_output=blog_output)
    
    response = model.invoke(formatted_prompt)
    
    try:
        content_str = (response.content
                      .strip('```')
                      .strip('json')
                      .strip())
        
        visuals_json = json.loads(content_str)
        render_visuals(visuals_json.get("visuals", []))
        
    except json.JSONDecodeError as e:
        print(f"JSON Parsing Error: {e}")