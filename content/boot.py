import board
from storage import disable_usb_drive, remount
from digitalio import DigitalInOut, Direction, Pull
from time import sleep
from supervisor import disable_autoreload

############################################################################################
# Constants for configuration
SWITCH_PIN = board.GP1  # Pin for the USB mount switch
SLEEP_TIME = 0.05      # Sleep time after initializing switch

# Initializes a switch and returns the switch instance
def _init_switch(pin):
    switch = DigitalInOut(pin)
    switch.direction = Direction.INPUT
    switch.pull = Pull.UP
    sleep(SLEEP_TIME)
    return switch

# Checks if a switch is pressed (inverse logic, returns True if pressed)
def _is_switch_pressed(switch):
    return switch.value == False  # Switch logic is inverted

############################################################################################

# Initialize the USB mount switch
_switch_mount_usb = _init_switch(SWITCH_PIN)

############################################################################################

# Disable auto-reload to prevent firmware from resetting
disable_autoreload()

# If switch is not pressed, disable USB drive and remount it in read-write mode
if not _is_switch_pressed(_switch_mount_usb):
    disable_usb_drive()
    remount("/", readonly=False)
