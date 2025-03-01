from pythonosc import dispatcher, osc_server
from handler_factory import HandlerFactory
from logger import log
from config import get_config

CONFIG = {} # Global

def handle_msg(client_address, address, *args):
    """ Gets called when a mesage is received by the OSC Server"""
    caller_full_ip = f"{client_address[0]}:{client_address[1]}"
    
    log.info(f"Message received [{caller_full_ip}] '{address}' {args}")

    handler = HandlerFactory.get_handler(address)
    
    if handler:
        handler.handle(address, *args)
    else:
        log.warning(f"Message without handler [{caller_full_ip}] '{address}' {args}")

def startServer():
    """ Config and execute the OSC Server """

    ip = get_config("server_ip")            # Server ip, this IP will works for localhost.
    port = int(get_config("server_port"))   # Port in case you have more than one OSC Server.

    # Dispatcher configuration to assign halders for the msgs
    disp = dispatcher.Dispatcher()
    disp.set_default_handler(handle_msg, True)

    # Server start
    server = osc_server.ThreadingOSCUDPServer((ip, port), disp)
    log.info(f"OSC Server started in {ip}:{port}")
    server.serve_forever()  # Mantiene el servidor activo

if __name__ == "__main__":
    startServer()