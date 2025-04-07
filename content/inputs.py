from pyswitch.clients.kemper.actions.amp import AMP_GAIN
from pyswitch.clients.kemper.actions.tempo import TAP_TEMPO, SHOW_TEMPO
from pyswitch.clients.kemper.actions.effect_state import EFFECT_STATE
from pyswitch.clients.kemper.actions.bank_up_down import BANK_UP, BANK_DOWN
from pyswitch.clients.kemper.actions.rig_select import RIG_SELECT
from pyswitch.clients.kemper.actions.tuner import TUNER_MODE
from pyswitch.clients.local.actions.encoder_button import ENCODER_BUTTON
from pyswitch.clients.kemper import KemperEffectSlot
from display import DISPLAY_HEADER_1, DISPLAY_HEADER_2, DISPLAY_FOOTER_1, DISPLAY_FOOTER_2, DISPLAY_RIG_NAME
from pyswitch.hardware.devices.pa_midicaptain_10 import *

# Actions setup
_accept = ENCODER_BUTTON()
_cancel = ENCODER_BUTTON()

# Helper function to create EFFECT_STATE action
def create_effect_state_action(slot_id, display):
    return EFFECT_STATE(
        slot_id=slot_id, 
        display=display
    )

# Helper function to create RIG_SELECT action
def create_rig_select_action(rig, display_mode=RIG_SELECT_DISPLAY_TARGET_RIG):
    return RIG_SELECT(
        rig=rig, 
        display_mode=display_mode
    )

# Inputs Setup
Inputs = [
    {
        "assignment": PA_MIDICAPTAIN_10_WHEEL_ENCODER,
        "actions": [
            AMP_GAIN(
                accept_action=_accept, 
                cancel_action=_cancel, 
                preview_display=DISPLAY_RIG_NAME, 
                step_width=40
            ),
        ]
    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_1,
        "actions": [create_effect_state_action(KemperEffectSlot.EFFECT_SLOT_ID_A, DISPLAY_HEADER_1)]
    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_2,
        "actions": [create_effect_state_action(KemperEffectSlot.EFFECT_SLOT_ID_B, DISPLAY_HEADER_2)]
    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_3,
        "actions": [create_effect_state_action(KemperEffectSlot.EFFECT_SLOT_ID_C, DISPLAY_FOOTER_1)]
    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_4,
        "actions": [create_effect_state_action(KemperEffectSlot.EFFECT_SLOT_ID_D, DISPLAY_FOOTER_2)]
    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_UP,
        "actions": [
            TAP_TEMPO(use_leds=False),
            SHOW_TEMPO(text='Tempo')
        ],
        "actionsHold": [
            TUNER_MODE(use_leds=False, text='Tuner')
        ]
    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_A,
        "actionsHold": [
            BANK_DOWN(display_mode=RIG_SELECT_DISPLAY_TARGET_RIG, text='Bank dn')
        ],
        "actions": [create_rig_select_action(1)]
    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_B,
        "actions": [create_rig_select_action(2)]
    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_C,
        "actions": [create_rig_select_action(3)]
    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_D,
        "actions": [create_rig_select_action(4)]
    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_DOWN,
        "actionsHold": [
            BANK_UP(display_mode=RIG_SELECT_DISPLAY_TARGET_RIG, text='Bank up')
        ],
        "actions": [create_rig_select_action(5)]
    },
    {
        "assignment": PA_MIDICAPTAIN_10_WHEEL_BUTTON,
        "actions": [_accept],
        "actionsHold": [_cancel]
    }
]
