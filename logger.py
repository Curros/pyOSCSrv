import logging
from config import get_config

# Get the log lvl from the .vscode/launch.json
log_level = get_config("server_log_level").upper()

# Check if the value is valid.
valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
if log_level not in valid_levels:
    log_level = "INFO"  # Default value in case the one setted is not valid.

# Configuration
logging.basicConfig(
    level=log_level,  # Valid lvls (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s|%(levelname)s| %(message)s",  # Formato con fecha y nivel
    datefmt="%Y-%m-%d|%H:%M:%S",  # Formato de fecha y hora
)

# Logger creation
log = logging.getLogger(__name__)