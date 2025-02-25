from abc import ABC, abstractmethod

class BaseHandler(ABC):
    @abstractmethod
    def handle(self, address, *args):
        """Required method to be implement in all handlers"""