import os
import json
from datetime import datetime

def save_state(state, directory="outputs"):
    os.makedirs(directory, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(directory, f"run_{timestamp}.json")
    with open(path, "w") as f:
        json.dump(state, f, indent=2)
    return path
