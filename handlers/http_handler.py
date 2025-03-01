from handlers.base_handler import BaseHandler
from logger import log

class HttpHandler(BaseHandler):
    def handle(self, address, *args):

        if args:
            last_arg = args[-1]  # Guarda el último argumento
            args = args[:-1]  # Elimina el último elemento
            log.debug(f"Last Arg: {last_arg}")
            log.debug(f"Cleaned Args: {args}")

        if not args:
            log.warning("No arguments provided.")
            return # No action executed.
        
        try:
            address_lst = address.split("/")

            if len(address_lst) < 2:
                log.warning(f"Need some development.")
                pass  # For future needs.

            return
        except Exception as e:
            log.error(f"Error executing {address}: {e}")