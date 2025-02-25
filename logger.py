import logging
import os

# Get the log lvl from the .vscode/launch.json
log_level = os.getenv("LOG_LEVEL", "INFO").upper()

# Check if the value is valid.
valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
if log_level not in valid_levels:
    log_level = "INFO"  # Valor predeterminado si no es válido

# Configuración del logger
logging.basicConfig(
    level=log_level,  # Valid lvls (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s|%(levelname)s| %(message)s",  # Formato con fecha y nivel
    datefmt="%Y-%m-%d|%H:%M:%S",  # Formato de fecha y hora
)

# Crear el logger
logger = logging.getLogger(__name__)
