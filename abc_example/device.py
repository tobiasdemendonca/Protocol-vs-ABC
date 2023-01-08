from abc import ABC, abstractmethod


class Device(ABC): 
    """Generic device that can be communicated with."""
    
    @abstractmethod
    def connect(self) -> None:
        pass
    
    @abstractmethod
    def disconnect(self) -> None: 
        pass
    
    @abstractmethod
    def send_message(self, message: str) -> None:
        pass
    
    @abstractmethod
    def get_status_update(self) -> str:
        pass
    
    