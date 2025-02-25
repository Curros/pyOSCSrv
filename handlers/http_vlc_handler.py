# handlers/vlc_handler.py
import requests
from logger import logger
from decouple import config
from handlers.http_handler import HttpHandler

class HttpVlcHandler(HttpHandler):
    def __init__(self):
        super().__init__()
        self.username = config("VLC_USERNAME", default="")  # VLC Lua username.
        self.password = config("VLC_PASSWORD", default="")  # VLC Lua password.
        self.base_url = "http://localhost:8080"  # URL VLC Server

    def handle(self, address, *args):
        # Split path to get the action ("/http/vlc/play")
        parts = address.split("/")
        if len(parts) >=3:
            action = parts[3] # Getting the action ("play")
        else:
            logger.warning("You need to specify an action.")
            return

        # Base param/action
        params = {"command": action}

        # Extra params from *args
        if args and len(args) > 1:
            clean_args = args[:-1] # We ignore the OSC arg at the end.
            for arg in clean_args:
                # Check correct format "key=val" and not the int that OSC send and the end.
                if not isinstance(arg, (int, float)) and "=" in arg:
                    key, value = arg.split("=", 1)
                    params[key] = value  # Add new param
                else:
                    logger.warning(f"Invalid argument: {arg}. Required format 'key=value'.")

        # Build full URL
        url = f"{self.base_url}/requests/status.json"
        url_full = f"{url}?{'&'.join([f'{k}={v}' for k, v in params.items()])}"
        
        logger.debug(f"URL used: [{url_full}]")

        # Request with HTTP basic auth
        try:
            response = requests.get(url, params=params, auth=(self.username, self.password))
            if response.status_code == 200:
                logger.info(f"Action [{action}] executed by VLC.")
            else:
                logger.error(f"HTTP Request error: {response.status_code}")

        except Exception as e:
            logger.error(f"Error with the HTTP request: {e}")
