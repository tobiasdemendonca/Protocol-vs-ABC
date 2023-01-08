import random

from device import Device


class SmartSpeaker(Device): 
    
    def __init__(self) -> None:
        self.id = random.Random().randint(0,100)

    def connect(self) -> None:
        print(f'Connecting to smart speaker of id {self.id}')
        
    def disconnect(self) -> None:
        print(f'Disconnected from smart speaker of id {self.id}')
        
    def send_message(self, message: str) -> None:
        print(f'Sent message {message}')
    
    def get_status_update(self) -> str:
        return f"All good from device with id: {self.id}"
        
        