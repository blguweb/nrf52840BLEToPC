from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService
import re
"""
@Description :   
@Author      :  kidominox 
@Time        :  2023/01/24
"""

radio = BLERadio()
ID = ['x6e', 'x52', 'x46', 'x35', 'x32', 'x38', 'x34', 'x30']

found = set()
device = None
message = None
buffer = 64

while True:
    if not device:
        print("scanning")
        for entry in radio.start_scan(ProvideServicesAdvertisement, timeout=60):
            if UARTService in entry.services:
                print("found a UARTService advertisement")
                # You can try a better method to pair your device
                s = repr(entry)
                s = re.findall(r'"(.+?)"',s)
                s = s[0]
                s = s[-31:].split("\\")
                if s == ID:
                    device = radio.connect(entry)
                    print("device connected!")                                                                                                                               
                    break
        # Stop scanning whether or not we are connected.
        radio.stop_scan()

    while device and device.connected:

        try:
            message = device[UARTService].read(buffer).decode()
        except OSError:
            try:
                uart_connection.disconnect()
            except:  # pylint: disable=bare-except
                pass
            uart_connection = None
        