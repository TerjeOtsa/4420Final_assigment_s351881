import json

def load_transport_modes(filepath):
    """Load transport modes from a JSON file."""
    with open(filepath, 'r') as file:
        return json.load(file)
