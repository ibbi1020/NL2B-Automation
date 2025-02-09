newsletter_text = ""
blog_output = ""

blog_prompt = f"""
    <<<Convert the following newsletter into a well-structured blog post while maintaining clarity, improving readability, and keeping the original intent intact. 
Ensure the content follows a logical flow and is engaging to read. 

Additionally, identify places where a **technical visual** (e.g., flowchart, process diagram, system architecture) would enhance understanding. Insert placeholders in the format [VISUAL_n: Brief description of what should be visualized]. 

Example:
- If the text describes a workflow, add [VISUAL_1: Workflow diagram showing the process].
- If the text contains a comparison, add [VISUAL_2: Comparison table or diagram].
- If the text discusses a system, add [VISUAL_3: Architecture diagram showing key components].

Here is the newsletter content:>>>

{newsletter_text}

<<<Ensure that all placeholders are appropriately placed and represent the right type of visuals.>>> 

"""

metadata_prompt = f"""
    <<<Based on the provided blog post, generate the following metadata in valid JSON format:

{{
    "title": "<A compelling and concise title>",
    "description": "<A 2-3 sentence summary that highlights the main idea>",
    "meta_title": "<A title optimized for search engines>",
    "meta_description": "<A brief meta description for SEO>",
    "tags": ["<5-10 relevant SEO tags>"],
    "slug": "<A URL-friendly slug based on the title>"
}}

Ensure that the metadata remains aligned with the content of the blog post. Here is the blog post:>>>

{blog_output}

<<<Output only valid JSON format, nothing else.>>>
"""

visual_prompt = f"""
You are an AI assistant that identifies placeholders in a blog post and generates **PyGraphviz** diagrams.

### Task:
1. Identify all placeholders in the format `[VISUAL_n: Description]` in the blog post.
2. Generate an **accurate** and **simple** Graphviz diagram for each.
3. Return the results in **valid JSON format**.

### **Example Output:**
Visuals:
- ID: "VISUAL_1"
  - Description: "Workflow diagram showing AI pipeline steps"
  - Graphviz Code: `digraph G <curly_brace> Newsletter -> Blog_Generator; Blog_Generator -> Mermaid_Generator; <curly_brace`
  - Caption: "AI pipeline for transforming newsletters into structured blogs."

- ID: "VISUAL_2"
  - Description: "Comparison table for different AI models"
  - Graphviz Code: `digraph G <curly_brace> GPT [shape=box]; DeepSeek [shape=ellipse]; GPT -> DeepSeek; <curly_brace>`
  - Caption: "Comparison between GPT and DeepSeek AI models."

### **Output Rules:**
- Output **only** valid JSON.
- Do **not** include explanations or extra text.

### **Blog Post:**
{blog_output}
"""