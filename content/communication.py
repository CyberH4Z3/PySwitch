##############################################################################################################################################
# Definition of communication wrappers. This is where the client-specific (i.e., Kemper) implementations are linked to the framework.
##############################################################################################################################################

# Import necessary components
from pyswitch.clients.kemper import KemperBidirectionalProtocol
from pyswitch.controller.midi import MidiRouting
from pyswitch.hardware.devices.pa_midicaptain import PA_MIDICAPTAIN_USB_MIDI

# Constants for configuration
DEFAULT_IN_CHANNEL = None  # All channels
DEFAULT_OUT_CHANNEL = 0
DEFAULT_PROTOCOL_TIME_LEASE_SECONDS = 30

# MIDI Devices in use
_USB_MIDI = PA_MIDICAPTAIN_USB_MIDI(
    in_channel=DEFAULT_IN_CHANNEL,
    out_channel=DEFAULT_OUT_CHANNEL
)

# Communication configuration
Communication = {
    # Optional: Protocol to use. If not specified, the standard Client protocol is used which requests all
    # parameters in each update cycle. Use this to implement bidirectional communication.
    "protocol": KemperBidirectionalProtocol(
        time_lease_seconds=DEFAULT_PROTOCOL_TIME_LEASE_SECONDS  # Time before re-initiating bidirectional communication
    ),

    # MIDI setup: Defines all MIDI routings for communication
    "midi": {
        "routings": [
            # Application: Receive MIDI messages from USB
            MidiRouting(
                source=_USB_MIDI,
                target=MidiRouting.APPLICATION
            ),
            # Application: Send MIDI messages to USB
            MidiRouting(
                source=MidiRouting.APPLICATION,
                target=_USB_MIDI
            ),
        ]
    }
}
