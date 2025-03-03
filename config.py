import os
import json

# Configuration path
CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")

# Default config
DEFAULT_CONFIG = {
    "server_ip": "0.0.0.0",
    "server_port": 8002,
    "server_log_level": "info",
    "vlc_username": "",
    "vlc_password": "pass",
    "vlc_server_address": "http://localhost:8080"
}


if os.path.exists(CONFIG_PATH):
    try:
        with open(CONFIG_PATH, "r") as f:
            CONFIG = json.load(f)
    except json.JSONDecodeError:
        CONFIG = {}
else:
    CONFIG = {}


# Allow calling config in any place
def get_config(key):

    if key.upper() in os.environ:
        return os.getenv(key.upper())

    if key in CONFIG:
        return CONFIG[key]

    if key in DEFAULT_CONFIG:
        CONFIG[key] = DEFAULT_CONFIG[key]   # Add missing key
        save_config()                       # Save key
        return DEFAULT_CONFIG[key]

    raise KeyError((f"Configutation key '{key}' not found."))


def save_config():
    """Save default config in config.json"""
    with open(CONFIG_PATH, "w") as f:
        json.dump(CONFIG, f, indent=4)
