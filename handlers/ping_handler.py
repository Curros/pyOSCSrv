from handlers.base_handler import BaseHandler
from logger import logger

class PingHandler(BaseHandler):
    def handle(self, address, *args):
        logger.info("Ping recibido, respondiendo...")
