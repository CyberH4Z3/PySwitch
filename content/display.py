from pyswitch.clients.kemper import KemperRigNameCallback
from pyswitch.clients.kemper import TunerDisplayCallback
from micropython import const
from pyswitch.misc import DEFAULT_LABEL_COLOR
from pyswitch.ui.ui import DisplayElement
from pyswitch.ui.ui import DisplayBounds
from pyswitch.ui.elements import DisplayLabel
from pyswitch.ui.elements import BidirectionalProtocolState

# Constants
_DISPLAY_WIDTH = const(240)
_DISPLAY_HEIGHT = const(240)
_SLOT_WIDTH = const(120)
_SLOT_HEIGHT = const(40)
_FOOTER_Y = const(200)
_RIG_NAME_HEIGHT = const(160)

# Layout Template for Labels
_ACTION_LABEL_LAYOUT = {
    "font": "/fonts/H20.pcf",
    "backColor": DEFAULT_LABEL_COLOR,
    "stroke": 1,
}

# Reusable function to create DisplayLabel
def create_display_label(x, y, w, h, layout=_ACTION_LABEL_LAYOUT):
    return DisplayLabel(
        layout=layout,
        bounds=DisplayBounds(x=x, y=y, w=w, h=h)
    )

# Display Elements
DISPLAY_HEADER_1 = create_display_label(0, 0, _SLOT_WIDTH, _SLOT_HEIGHT)
DISPLAY_HEADER_2 = create_display_label(_SLOT_WIDTH, 0, _SLOT_WIDTH, _SLOT_HEIGHT)

DISPLAY_FOOTER_1 = create_display_label(0, _FOOTER_Y, _SLOT_WIDTH, _SLOT_HEIGHT)
DISPLAY_FOOTER_2 = create_display_label(_SLOT_WIDTH, _FOOTER_Y, _SLOT_WIDTH, _SLOT_HEIGHT)

# Rig Name Display Label with custom layout
DISPLAY_RIG_NAME = DisplayLabel(
    bounds=DisplayBounds(
        x=0, y=_SLOT_HEIGHT, w=_DISPLAY_WIDTH, h=_RIG_NAME_HEIGHT
    ),
    layout={
        "font": "/fonts/PTSans-NarrowBold-40.pcf",
        "lineSpacing": 0.8,
        "maxTextWidth": 220,
        "text": KemperRigNameCallback.DEFAULT_TEXT,
    },
    callback=KemperRigNameCallback(show_rig_id=True)
)

# Splashes
Splashes = TunerDisplayCallback(
    splash_default=DisplayElement(
        bounds=DisplayBounds(x=0, y=0, w=_DISPLAY_WIDTH, h=_DISPLAY_HEIGHT),
        children=[
            DISPLAY_HEADER_1,
            DISPLAY_HEADER_2,
            DISPLAY_FOOTER_1,
            DISPLAY_FOOTER_2,
            DISPLAY_RIG_NAME,
            BidirectionalProtocolState(
                bounds=DisplayBounds(
                    x=0, y=_SLOT_HEIGHT, w=_DISPLAY_WIDTH, h=_RIG_NAME_HEIGHT
                )
            ),
        ]
    )
)
