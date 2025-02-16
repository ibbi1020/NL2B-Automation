# NL2B-Automation

## Overview
NL2B Automation transforms text-based newsletters into blog posts. The project uses a combination of Python and Streamlit to provide a user interface for generating structured blog content from unstructured text. It also includes utilities for AI-based model prompts and visualization rendering.

## Features
- Converts newsletters into blog posts using AI models.
- Generates metadata for blog posts.
- Creates visualizations with Python code (using NetworkX and matplotlib).
- Supports local environment setup through a virtual environment.

## Prerequisites
1. Python 3.9+  
2. OpenAI API key (required for certain models). Set it in your environment variables as:
```
OPENAI_API_KEY=<your_key_here>
```

4. VS Code or a similar IDE for editing and running the app.

## Installation
1. Clone this repository or download the source code.  
2. Create a virtual environment:
```
python -m venv .venv
```
3. Activate the virtual environment (Windows):
```
.\.venv\Scripts\Activate.ps1
```
4. 
```
pip install -r requirements.txt
```

## Usage
0. (IF USING OLLAMA) Add your desired Ollama model name to bot_local variable in bots.py
1. Launch the Streamlit app:
```
streamlit run app.py
```
2. Enter your newsletter text in the text area, then click Generate Blog.
3. For visualizations, ensure Graphviz is correctly installed

## Troubleshooting
- If scripts fail to run on Windows, set execution policy:
```
Set-ExecutionPolicy RemoteSigned
```
- If AI calls fail, verify your OpenAI key is correctly set.
- For missing Graphviz executables, install Graphviz and add it to your system PATH.
