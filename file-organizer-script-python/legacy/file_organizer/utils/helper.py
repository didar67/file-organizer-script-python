"""
This module loads YAML configuration and provides helper utilities
for the File Organizer script.
"""

import yaml
import os


def load_config(config_path: str = "config/config.yaml") -> dict:
    """
    Load and return YAML configuration data from the specified path.

    Args:
        config_path (str): Path to YAML configuration file.

    Returns:
        dict: Dictionary containing configuration data.

    Raises:
        FileNotFoundError: If the YAML config file does not exist.
        yaml.YAMLError: If the file contains invalid YAML syntax.
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    with open(config_path, "r", encoding="utf-8") as file:
        try:
            data = yaml.safe_load(file)
            return data
        except yaml.YAMLError as e:
            raise yaml.YAMLError(f"Error parsing YAML config: {e}")


# Quick test (optional)
if __name__ == "__main__":
    config = load_config()
    print("Configuration Loaded Successfully!")
    print(config)
