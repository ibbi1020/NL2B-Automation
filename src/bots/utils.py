import os
import matplotlib.pyplot as plt
import networkx as nx
from typing import List, Dict
from ..config.settings import OUTPUT_DIR

def render_visuals(visuals_json: List[Dict], output_dir: str = OUTPUT_DIR) -> None:
    """
    Executes Python visualization code from JSON and saves outputs locally.
    
    Args:
        visuals_json (List[Dict]): List of visual configurations
        output_dir (str): Directory to save the output files
    """
    os.makedirs(output_dir, exist_ok=True)

    for visual in visuals_json:
        visual_id = visual["id"]
        python_code = visual["python_code"]
        output_path = os.path.join(output_dir, f"{visual_id}.png")

        if 'plt.savefig("outputs")' not in python_code:
            python_code += f"\nplt.savefig('{output_path}')\nplt.close()"
        else:
            python_code = python_code.replace(
                'plt.savefig("outputs")', 
                f'plt.savefig("{output_path}")'
            )

        try:
            exec(python_code, {"plt": plt, "nx": nx, "__builtins__": {}})
            print(f"Generated: {output_path}")
        except Exception as e:
            print(f"Error generating {visual_id}: {e}")