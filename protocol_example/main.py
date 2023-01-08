from typing import Protocol

from devices import SmartSpeaker


class Device(Protocol):
    
    def connect(self) -> None:
        ...
    
    def disconnect(self) -> None: 
        ...
    
    def send_message(self, message: str) -> None:
        ...
    

def communicator(device: Device):
    device.connect()
    device.send_message(message='turn on please')
    

if __name__ == "__main__":
    speaker = SmartSpeaker()
    communicator(speaker)