import os, sys

if os.name == "nt":
    import msvcrt

    def getch():
        return msvcrt.getch().decode()

else:
    import tty, termios

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    tty.setraw(sys.stdin.fileno())

    def getch():
        return sys.stdin.read(1)


os.sys.path.append("./DynamixelSDK/python/src")  # Path setting

import dynamixel_sdk as dynamixel # Uses Dynamixel SDK library
print(dir(dynamixel))
# Model XL330-M288

DXL_ID = 1
BAUDRATE                    = 57600
DEVICENAME                  = "/dev/ttyUSB0".encode('utf-8')

PROTOCOL_VERSION = 2

ADDR_PRO_PRESENT_POSITION    = 132

TORQUE_ENABLE               = 1                             # Value for enabling the torque
TORQUE_DISABLE              = 0                             # Value for disabling the torque
DXL_MINIMUM_POSITION_VALUE  = -150000                       # Dynamixel will rotate between this value
DXL_MAXIMUM_POSITION_VALUE  = 150000                        # and this value (note that the Dynamixel would not move when the position value is out of movable range. Check e-manual about the range of the Dynamixel you use.)
DXL_MOVING_STATUS_THRESHOLD = 20                            # Dynamixel moving status threshold

ESC_ASCII_VALUE             = 0x1b

COMM_SUCCESS                = 0                             # Communication Success result value
COMM_TX_FAIL                = -1001                         # Communication Tx Failed

# Initialize PortHandler Structs
# Set the port path
# Get methods and members of PortHandlerLinux or PortHandlerWindows
from dynamixel.driver import (
    DynamixelDriver,
    DynamixelDriverProtocol,
    FakeDynamixelDriver,
)

driver : DynamixelDriverProtocol
