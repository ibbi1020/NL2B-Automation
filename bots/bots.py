# import the required libraries
from langchain_openai import ChatOpenAI
from langchain.globals import set_debug
from langchain.prompts import PromptTemplate
import matplotlib.pyplot as plt
import networkx as nx
import json
import prompts
import os

# get openai key from environment variable
import os
openai_key = os.environ.get("OPENAI_API_KEY")
if openai_key is None:
    raise ValueError("Please set OPENAI_API_KEY environment variable")

bot_local = ""
bot_remote = "gpt-4o"

## BOT FUNCTIONS

def render_visuals(visuals_json, output_dir="./outputs"):
    """Executes Python visualization code from JSON and saves outputs locally."""
    os.makedirs(output_dir, exist_ok=True)  # Ensure the output folder exists

    for visual in visuals_json:
        visual_id = visual["id"]
        python_code = visual["python_code"]  # Extract code

        # Define output file path
        output_path = os.path.join(output_dir, f"{visual_id}.png")

        # Check if {output_path} is present in the code before formatting
        if 'plt.savefig("outputs")' not in python_code:
            print(f"Warning: {visual_id} does not contain '{{output_path}}'. Using default output path.")
            python_code = python_code + f"\nplt.savefig('{output_path}')\nplt.close()"
        else:
            python_code = python_code.replace('plt.savefig("outputs")', f'plt.savefig("{output_path}")')

        # Execute the visualization code
        try:
            exec(python_code, {"plt": plt, "nx": nx, "__builtins__": {}})
            print(f"Generated: {output_path}")
        except Exception as e:
            print(f"Error generating {visual_id}: {e}")
    

def generate_blog(nl_text):
    """Generates a blog from the given newsletter text"""
    
    model = ChatOpenAI(model =bot_remote, temperature = 0)
    
    prompt = prompts.blog_prompt.format(newsletter_text = nl_text)
    
    response = []
    for chunk in model.stream(prompt):
        response.append(chunk)

    return response

def generate_metadata(blog_output):
    """Generates metadata for blog based on initial blog output"""
    
    model = ChatOpenAI(model = bot_remote, temperature = 0)
    
    prompt = prompts.metadata_prompt.format(blog_output = blog_output)
    
    response = model.invoke(prompt)
    return response

def generate_visuals(blog_output):
    """Identifies placeholders in the blog and generates JSON for diagrams <library TBD>"""
    
    model = ChatOpenAI(model=bot_remote, temperature=0)
    
    #Fetch prompt template
    visuals_prompt = PromptTemplate.from_template(prompts.visual_prompt)
    
    # Format the prompt
    formatted_prompt = visuals_prompt.format(blog_output=blog_output)
    
    # Generate response
    response = model.invoke(formatted_prompt)
    
    # Parse response into JSON format
    try:
        # Clean output from leading and trailing characters
        content_str = response.content.strip('```')
        content_str = content_str.strip('json')
        content_str = content_str.strip()
        
        # load JSON 
        visuals_json = json.loads(content_str)
        
        # Call render function
        render_visuals(visuals_json.get("visuals", [])) #call render function 
        
    except json.JSONDecodeError as e:
        print(f"JSON Parsing Error: {e}")


