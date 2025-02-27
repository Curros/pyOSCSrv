from pythonosc import dispatcher, osc_server
from handler_factory import HandlerFactory
from logger import logger
import os

def handle_msg(client_address, address, *args):
    """ Gets called when a mesage is received by the OSC Server"""
    caller_ip = f"{client_address[0]}:{client_address[1]}"
    logger.info(f"Message received [{caller_ip}] '{address}' {args}")

    handler = HandlerFactory.get_handler(address)
    
    if handler:
        handler.handle(address, *args)
    else:
        logger.warning(f"Message without handler [{caller_ip}] '{address}' {args}")

def startServer():
    """ Config and execute the OSC Server """

    ip = os.getenv("SERVER_IP", "0.0.0.0") # Server ip, this IP will works for localhost.
    port = int(os.getenv("SERVER_PORT", 8002))   # Port in case you have more than one OSC Server.

    # Dispatcher configuration to assign halders for the msgs
    disp = dispatcher.Dispatcher()
    disp.set_default_handler(handle_msg, True)

    # Server start
    server = osc_server.ThreadingOSCUDPServer((ip, port), disp)
    logger.info(f"OSC Server started in {ip}:{port}")
    server.serve_forever()  # Mantiene el servidor activo

if __name__ == "__main__":
    startServer()