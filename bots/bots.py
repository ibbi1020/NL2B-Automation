# import the required libraries
from langchain_openai import ChatOpenAI
from langchain.globals import set_debug
from langchain.output_parsers import JsonOutputKeyToolsParser
from langchain.prompts import PromptTemplate
import json
import prompts
import graphviz

# get openai key from environment variable
import os
openai_key = os.environ.get("OPENAI_API_KEY")
if openai_key is None:
    raise ValueError("Please set OPENAI_API_KEY environment variable")

set_debug(True)


## BOT FUNCTIONS

def render_visuals(visuals_json, output_dir="outputs"):
    """Renders the visuals from JSON using PyGraphviz"""
    os.makedirs("visuals", exist_ok=True)
    
    visuals = visuals_json.get("visuals", [])
    
    for visual in visuals:
        visual_id = visual["id"]
        description = visual["description"]
        graphviz_code = visual["graphviz_code"]
        
        output_path = f"{output_dir}/{visual_id}.png"
        
        #create graphviz object
        dot = graphviz.Source(graphviz_code)
        dot.render(output_path, format="png")  # Saves as PNG

        print(f"Generated: {output_path}.png")
    

def generate_blog(newsletter_text):
    """Generates a blog from the given newsletter text"""
    model = ChatOpenAI(model ="gpt-3.5-turbo",
                   temperature = 0)
    
    prompt = prompts.blog_prompt.format(newsletter_text = newsletter_text)
    
    response = []
    for chunk in model.stream(prompt):
        response.append(chunk)
        #print(chunk.content, flush=True)

    return response

def generate_metadata(blog_output):
    """Generates metadata for blog based on initial blog output"""
    
    model = ChatOpenAI(model ="gpt-3.5-turbo",
                   temperature = 0)
    
    prompt = prompts.metadata_prompt.format(blog_output = blog_output)
    
    response = model.invoke(prompt)
    return response

def generate_visuals(blog_output):
    """Identifies placeholders in the blog and generates Mermaid diagrams"""
    
    model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    
    # Define expected JSON output schema
    expected_schema = {
        "visuals": [
            {
                "id": "string",
                "description": "string",
                "mermaid_code": "string",
                "caption": "string"
            }
        ]
    }
    
    parser = JsonOutputKeyToolsParser(key_name="visuals")  # Ensures "visuals" key is present
    
    visuals_prompt = PromptTemplate.from_template(prompts.visual_prompt)
    
    print("DEBUG: Visuals Prompt: ", visuals_prompt)
    # Format the prompt
    formatted_prompt = visuals_prompt.format(blog_output=blog_output)
    
    # Generate response
    response = model.invoke(formatted_prompt)
    print(response.content)
    
    # Parse response into JSON format
    try:
        visuals_json = json.loads(response.content)
        return visuals_json.get("visuals", [])  # Avoid KeyError
    except json.JSONDecodeError as e:
        print(f"JSON Parsing Error: {e}")
        return []

    return visuals_json

