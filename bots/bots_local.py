# import the required libraries
from langchain_ollama import ChatOllama
from langchain.globals import set_debug
from langchain.prompts import PromptTemplate
import matplotlib.pyplot as plt
import networkx as nx
import json
import prompts
import os

set_debug(True)


## BOT FUNCTIONS

def render_visuals(visuals_json, output_dir="output"):
    """Executes Python visualization code from JSON and saves outputs locally."""
    os.makedirs(output_dir, exist_ok=True)  # Ensure the output folder exists

    visuals = visuals_json.get("visuals", [])

    for visual in visuals:
        visual_id = visual["id"]
        python_code = visual["python_code"]  # Extract code

        # Define output file path
        output_path = os.path.join(output_dir, f"{visual_id}.png")

        # Check if {output_path} is present in the code before formatting
        if 'plt.savefig("outputs")' not in python_code:
            print(f"Warning: {visual_id} does not contain '{{output_path}}'. Using default output path.")
            python_code = python_code + f"\nplt.savefig('{output_path}')\nplt.close()"

        # Execute the visualization code
        try:
            exec(python_code, {"plt": plt, "nx": nx, "__builtins__": {}})  # Provide plt and nx explicitly
            print(f"Generated: {output_path}")
        except Exception as e:
            print(f"Error generating {visual_id}: {e}")
    

def generate_blog(newsletter_text):
    """Generates a blog from the given newsletter text"""
    model = ChatOllama(model ="deepseek-r1:8b",
                   temperature = 0)
    
    prompt = prompts.blog_prompt.format(newsletter_text = newsletter_text)
    
    response = model.invoke(prompt)
    return response

def generate_metadata(blog_output):
    """Generates metadata for blog based on initial blog output"""
    
    model = ChatOllama(model ="deepseek-r1:8b",
                   temperature = 0)
    
    prompt = prompts.metadata_prompt.format(blog_output = blog_output)
    
    response = model.invoke(prompt)
    return response

def generate_visuals(blog_output):
    """Identifies placeholders in the blog and generates JSON for diagrams <library TBD>"""
    
    model = ChatOllama(model="deepseek-r1:8b", temperature=0)
    
    #Fetch prompt template
    visuals_prompt = PromptTemplate.from_template(prompts.visual_prompt)
    
    # Format the prompt
    formatted_prompt = visuals_prompt.format(blog_output=blog_output)
    
    # Generate response
    response = model.invoke(formatted_prompt)
    print(response.content)
    
    # Parse response into JSON format
    try:
        # Parse JSON
        visuals_json = json.loads(response.content)
        render_visuals(visuals_json.get("visuals", [])) #call render function 
        #return visuals_json.get("visuals", [])  # Avoid KeyError
    except json.JSONDecodeError as e:
        print(f"JSON Parsing Error: {e}")
        return []

    return visuals_json

