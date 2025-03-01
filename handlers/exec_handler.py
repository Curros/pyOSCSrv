# handlers/exec_handler.py
import subprocess
from handlers.base_handler import BaseHandler
from logger import log

class ExecHandler(BaseHandler):
    def handle(self, address, *args):

        if args:
            last_arg = args[-1]  # Save the last argument
            args = args[:-1]  # Delete last argument
            log.debug(f"Last Arg: {last_arg}")
            log.debug(f"Cleaned Args: {args}")

        if not args:
            log.warning("No arguments provided.")
            return # No action executed.

        try:
            app = args[0]
            params = args[1:]

            if app.endswith(".ps1"):  # Execute PowerShell script
                subprocess.run(["pwsh", "-ExecutionPolicy", "Bypass", "-File", app, *map(str, params)], check=True)
            
            elif (app.endswith(".exe")):  # Execute windows app
                subprocess.run([app, *map(str, params)], shell=True, check=True)

            else:
                log.warning("No proper param provided.")
                return
        
        except Exception as e:
            log.error(f"Error executing {address}: {e}")
