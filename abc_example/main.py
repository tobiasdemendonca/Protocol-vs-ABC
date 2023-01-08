from device import Device
from devices import SmartSpeaker


def communicator(device: Device):
    device.connect()
    device.send_message(message='turn on please')
    


if __name__ == "__main__":
    """Try commenting out an abstract method in device.py. 
    Then comment out a method in devices.py. You should see by the linting
    (use "python.analysis.typeCheckingMode": "basic" to see it linted in VSCode settings)
    that you won't be able to create an object if it doesn't implement all methods in the abstract base class.
    
    If you wanted to separate out the methods into different interfaces, you'd have to
    go down a multiple inheritance route."""
    speaker = SmartSpeaker() 
    communicator(device=speaker)