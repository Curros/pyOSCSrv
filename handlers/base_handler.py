# handlers/base_handler.py
from abc import ABC, abstractmethod

class BaseHandler(ABC):
    @abstractmethod
    def handle(self, address, *args):
        """Método que debe ser implementado en cada handler"""
        print(f"Message: [{address}] Args: [{''.join(map(str,args))}]")
