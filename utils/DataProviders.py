import json
from pathlib import Path


def resd_json_file(filepath):
    with open(filepath) as f:
        data_list = json.load(f)
        return data_list