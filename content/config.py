##############################################################################################################################################
# Firmware processing configuration. Most options are optional.
##############################################################################################################################################

# Constants for configuration parameters to avoid repetition and improve readability.
DEFAULT_MIDI_BUFFER_CLEAR = True
DEFAULT_MAX_REQUEST_LIFETIME_MS = 2000
DEFAULT_UPDATE_INTERVAL_MS = 200
DEFAULT_MEMORY_WARN_LIMIT_BYTES = 1024 * 15  # 15kB memory threshold for warning
DEFAULT_ENABLE_MIDI_BRIDGE = True
DEFAULT_LED_BRIGHTNESS_ON = 0.3
DEFAULT_LED_BRIGHTNESS_OFF = 0.02
DEFAULT_DISPLAY_DIM_FACTOR_ON = 1
DEFAULT_DISPLAY_DIM_FACTOR_OFF = 0.2

# Configuration dictionary
Config = {
    # Max. number of MIDI messages being parsed before the next switch state evaluation
    # is triggered. If set to 0, only one message is parsed per tick, which leads to 
    # flickering states sometimes. If set too high, switch states will not be read for too long.
    # A good value is the maximum amount of switches. Default is 10.
    # "maxConsecutiveMidiMessages": 10,

    # Clear MIDI buffer before starting processing. Default is True.
    "clearBuffers": DEFAULT_MIDI_BUFFER_CLEAR,

    # Max. milliseconds until a request is being terminated and assumed that the Kemper device is offline.
    # Optional, default is 2 seconds (2000 milliseconds).
    "maxRequestLifetimeMillis": DEFAULT_MAX_REQUEST_LIFETIME_MS,

    # Update interval, for updating rig date and other displays (milliseconds). Default is 200.
    "updateInterval": DEFAULT_UPDATE_INTERVAL_MS,

    # Amount of bytes that must at least be free at the time processing starts.
    # Default threshold for the warning is 15kB.
    "memoryWarnLimitBytes": DEFAULT_MEMORY_WARN_LIMIT_BYTES,

    # Enables file transfer via MIDI from and to the device using PyMidiBridge.
    # Disabling this reduces memory usage by about 11kB.
    "enableMidiBridge": DEFAULT_ENABLE_MIDI_BRIDGE,

    # Globally used brightness values for the LEDs.
    # Note that not all action definitions in kemper.py or other client implementations may regard this.
    # "ledBrightnessOn": DEFAULT_LED_BRIGHTNESS_ON,
    # "ledBrightnessOff": DEFAULT_LED_BRIGHTNESS_OFF,

    # Globally used dim factors for the DisplayLabels.
    # "displayDimFactorOn": DEFAULT_DISPLAY_DIM_FACTOR_ON,
    # "displayDimFactorOff": DEFAULT_DISPLAY_DIM_FACTOR_OFF,

    ## Development Options ###################################################################################################################

    # Optional, shows the effect slot names in the display labels for EffectEnableAction
    # "showEffectSlotNames": True,

    # Debug output options. Uncomment to enable.
    # "debugStats": True,                            # Show info about runtime and memory usage periodically
    # "debugStatsInterval": 2000,                    # Update interval for runtime statistics
    # "debugBidirectionalProtocol": True,            # Debug bidirectional protocol, if any
    # "debugUnparsedMessages": True,                 # Show all unparsed MIDI messages
    # "debugSentMessages": True,                     # Show all sent messages
    # "excludeMessageTypes": ["SystemExclusive"],    # Types to exclude from "debugUnparsedMessage"
    # "debugClientStats": True,                      # Periodically shows client information

    # When a ClientParameterMapping instance is set here, incoming messages for this mapping will be shown.
    # "debugMapping": MAPPING_MORPH_PEDAL(),

    # Explore Mode: Set this to True to boot into explore mode.
    # This mode listens to all GPIO pins available and outputs the ID of the last pushed one,
    # and also rotates through all available NeoPixels.
    # "exploreMode": True
}
