import subprocess
from handlers.base_handler import BaseHandler
from logger import log

class TaskkillHandler(BaseHandler):
    def handle(self, address, *args):
        if not args:
            log.warning("No application name provided for taskkill.")
            return

        app_name = args[0]  # Firs argument, process name.

        try:
            log.info(f"Attempting to kill process: {app_name}")
            subprocess.run(["taskkill", "/F", "/IM", app_name], check=True, capture_output=True, text=True)
            log.info(f"Successfully killed {app_name}")

        except subprocess.CalledProcessError as e:
            log.error(f"Failed to kill {app_name}: {e.stderr.rstrip("\n")}")
