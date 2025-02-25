import subprocess
from handlers.base_handler import BaseHandler
from logger import logger

class TaskkillHandler(BaseHandler):
    def handle(self, address, *args):
        if not args:
            logger.warning("No application name provided for taskkill.")
            return

        app_name = args[0]  # Firs argument, process name.

        try:
            logger.info(f"Attempting to kill process: {app_name}")
            subprocess.run(["taskkill", "/F", "/IM", app_name], check=True, capture_output=True, text=True)
            logger.info(f"Successfully killed {app_name}")

        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to kill {app_name}: {e.stderr.rstrip("\n")}")
