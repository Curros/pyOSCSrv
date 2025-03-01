from handlers.base_handler import BaseHandler
from logger import log

class PingHandler(BaseHandler):
    def handle(self, address, *args):
        log.info("Ping received, printing a pong...")
