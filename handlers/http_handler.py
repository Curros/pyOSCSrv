import subprocess
from handlers.base_handler import BaseHandler
from logger import logger

class HttpHandler(BaseHandler):
    def handle(self, address, *args):

        if args:
            last_arg = args[-1]  # Guarda el último argumento
            args = args[:-1]  # Elimina el último elemento
            logger.debug(f"Last Arg: {last_arg}")
            logger.debug(f"Cleaned Args: {args}")

        if not args:
            logger.warning("No arguments provided.")
            return # No action executed.
        
        try:
            address_lst = address.split("/")

            if len(address_lst) < 2:
                logger.warning(f"Need some development.")
                pass  # For future needs.

            return
        except Exception as e:
            logger.error(f"Error executing {address}: {e}")