# nrf52840BLEToPC
Use nrf52840(Seeed xiao ble) as the main control to connect various sensors, and transmit the sensor data to the computer for reception via Bluetooth.
# Configuration
1. The main control is Seeed XIAO BLE, and its chip is nrf52840, which is equipped with an arduino base, so the upper layer of the user uses the arduino IDE to program the code. 
  His Bluetooth part uses the Adafruit related library.
2. The PC part uses the Adafruit_CircuitPython_BLE library through practice, so it runs in linux, but not in windows for the time being. 
  OS: Ubuntu 20.04
# Process
## Install library
My python version is 3.8.
```bash
pip3 install adafruit-circuitpython-ble
```
If you need to install in a virtual environment, then

```bash
mkdir project-name && cd project-name
python3 -m venv .venv
source .venv/bin/activate
pip3 install adafruit-circuitpython-ble
```
### Test

```bash
from adafruit_ble import BLERadio

radio = BLERadio()
print("scanning")
found = set()
for entry in radio.start_scan(timeout=60, minimum_rssi=-80):
    addr = entry.address
    if addr not in found:
        print(entry)
    found.add(addr)

print("scan done")
```
official repository：[Adafruit_CircuitPython_BLE](https://github.com/adafruit/Adafruit_CircuitPython_BLE)

###  Search bluetooth and connect
The above demo is the part of retrieving Bluetooth. Through testing, we can easily retrieve the Bluetooth of nrf52840. Then make the connection:

```bash
radio.connect(entry)
```
Stop searching when you find it

```bash
radio.stop_scan()
```
### Data transmission
ntypes is the number of transmitted data, up to 64 by default, you can modify its buffer capacity in the UARTService class in the downloaded data package. 
There are three functions that can be used to read data:

```bash
def read(self, nbytes: Optional[int] = None) -> Optional[bytes]
def readinto(self, buf: WriteableBuffer, nbytes: Optional[int] = None) -> Optional[int]
def readline(self) -> Optional[bytes]
```
Writing data is:

```bash
def write(self, buf: ReadableBuffer) -> None
```
## Example

```bash
data = device[UARTService].read(ntypes)
message = data.decode()
```

