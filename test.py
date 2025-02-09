import json
from bots.bots import render_visuals

json_str = json_str = """
{
  "visuals": [
    {
      "id": "VISUAL_1",
      "description": "Workflow diagram showing AI pipeline steps",
      "graphviz_code": "digraph G { Newsletter -> Blog_Generator; Blog_Generator -> Mermaid_Generator; }",
      "caption": "AI pipeline for transforming newsletters into structured blogs."
    },
    {
      "id": "VISUAL_2",
      "description": "Decision tree for AI model selection",
      "graphviz_code": "digraph G { Start -> GPT [label=\\"Need Chatbot?\\"]; Start -> DeepSeek [label=\\"Need Code Generation?\\"]; GPT -> Finish; DeepSeek -> Finish; }",
      "caption": "Decision tree guiding AI model selection."
    },
    {
      "id": "VISUAL_3",
      "description": "Flowchart of data processing pipeline",
      "graphviz_code": "digraph G { Input_Data -> Preprocessing; Preprocessing -> Model_Training; Model_Training -> Evaluation; Evaluation -> Deployment; }",
      "caption": "A standard data pipeline from input to deployment."
    },
    {
      "id": "VISUAL_4",
      "description": "Comparison of AI frameworks",
      "graphviz_code": "graph G { PyTorch -- TensorFlow; TensorFlow -- JAX; PyTorch -- JAX; }",
      "caption": "Comparison between popular AI frameworks."
    }
  ]
}
"""

json_obj = json.loads(json_str)
render_visuals(json_obj)