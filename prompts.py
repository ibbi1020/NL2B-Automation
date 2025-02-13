newsletter_text = ""
blog_output = ""

blog_prompt = """
Convert the following newsletter into a well-structured blog post while maintaining clarity, improving readability, and keeping the original intent intact. 
Ensure the content follows a logical flow and is engaging to read. 

Additionally, identify places where a **technical visual** (e.g., flowchart, process diagram, system architecture) would enhance understanding. Insert placeholders in the format [VISUAL_n: Brief description of what should be visualized]. 

Example:
- If the text describes a workflow, add [VISUAL_1: Workflow diagram showing the process].
- If the text contains a comparison, add [VISUAL_2: Comparison table or diagram].
- If the text discusses a system, add [VISUAL_3: Architecture diagram showing key components].

Ensure that all placeholders are appropriately placed and represent the right type of visuals.
"""

metadata_prompt = """
Based on the provided blog post, generate the following metadata in valid JSON format:

{
    "title": "<A compelling and concise title>",
    "description": "<A 2-3 sentence summary that highlights the main idea>",
    "meta_title": "<A title optimized for search engines>",
    "meta_description": "<A brief meta description for SEO>",
    "tags": ["<5-10 relevant SEO tags>"],
    "slug": "<A URL-friendly slug based on the title>"
}

Ensure that the metadata remains aligned with the content of the blog post.
Output only valid JSON format, nothing else.
"""

visual_prompt = """
You are an AI assistant that identifies placeholders in a blog post and generates **Matplotlib + NetworkX** diagrams.

### Task:
1. Identify all placeholders in the format `[VISUAL_n: Description]` in the blog post.
2. Generate an **accurate** and **simple** NetworkX diagram for each.
3. Ensure the code **does NOT include import statements** for `matplotlib.pyplot` (`plt`) or `networkx` (`nx`).
4. Return the results in **valid JSON format**, where the key `"python_code"` contains the generated code.

### **Example Output:**
Visuals:
- ID: `"VISUAL_1"`
  - Description: `"Workflow diagram showing AI pipeline steps"`
  - Python Code:
    ```python
    G = nx.DiGraph()
    G.add_edges_from([
        ("Newsletter", "Blog Generator"),
        ("Blog Generator", "Mermaid Generator")
    ])

    plt.figure(figsize=(6, 4))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=2000, font_size=10)
    plt.savefig("outputs")
    plt.close()
    ```
  - Caption: `"AI pipeline for transforming newsletters into structured blogs."`

- ID: `"VISUAL_2"`
  - Description: `"Comparison between different AI models"`
  - Python Code:
    ```python
    G = nx.Graph()
    G.add_edges_from([
        ("GPT", "DeepSeek")
    ])

    plt.figure(figsize=(4, 4))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color="lightcoral", edge_color="black", node_size=2000, font_size=10)
    plt.savefig("outputs")
    plt.close()
    ```
  - Caption: `"Comparison between GPT and DeepSeek AI models."`

### **Output Rules:**
- Output **only** valid JSON.
- Do **not** include explanations or extra text.
- The `"python_code"` field **must be executable** without modifications.
- The code **must NOT** include any matplotlib or networkx import statements, any other necessary imports you are allowed to use.
- The code **must include `plt.savefig("outputs")`** to ensure the figure is saved correctly.
"""