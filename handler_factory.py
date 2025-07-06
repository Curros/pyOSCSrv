# handler_factory.py
from handlers.exec_handler import ExecHandler
from handlers.ping_handler import PingHandler
from handlers.taskkill_handler import TaskkillHandler
from handlers.spotify_handler import SpotifyHandler
from handlers.http_handler import HttpHandler
from handlers.http_vlc_handler import HttpVlcHandler

class HandlerFactory:
    @staticmethod
    def get_handler(address):
        
        if address.startswith("/exec"):
            return ExecHandler()
        elif address == "/ping":
            return PingHandler()
        elif address == "/taskkill":
            return TaskkillHandler()
        elif address.startswith("/spotify/"):
            return SpotifyHandler()
        elif address.startswith("/http"):
            address_lst = address.split("/")

            if len(address_lst) < 2:
                # We return the basic handler.
                return HttpHandler()
        
            app = address_lst[2]

            if app == "vlc":
                return HttpVlcHandler()  # Return handler for VLC
            else:
                return HttpHandler()
        else:
            return None  # If cant find any handler
