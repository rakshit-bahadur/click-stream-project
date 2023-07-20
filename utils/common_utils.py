import json

def read_json_config(file_path):
    """
    Read configuration from a JSON file and return it as a dictionary.

    Args:
        file_path (str): Path to the JSON configuration file.

    Returns:
        dict: Configuration as a dictionary.
    """
    with open(file_path, 'r') as file:
        config = json.load(file)
    return config
