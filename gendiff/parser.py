import os
import json
import yaml


def load_data_from_file(file_path):
    full_path = os.path.join(os.path.dirname(__file__), file_path)
    with open(full_path, 'r') as file:
        if file_path.endswith('.json'):
            return json.load(file)
        elif file_path.endswith('.yml') or file_path.endswith('.yaml'):
            return yaml.safe_load(file)
