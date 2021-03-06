import sys
from pathlib import Path

from virtualstudio.common.action_manager.actionmanager import registerCategoryIcon
from virtualstudio.common.structs.action.action_launcher import *
from virtualstudio.common.tools.icontools import readPNGIcon
from virtualstudio2.plugins.debugaction.actions.button_debug_action import ButtonDebugAction
from virtualstudio2.plugins.debugaction.actions.fader_debug_action import FaderDebugAction
from virtualstudio2.plugins.debugaction.actions.imagebutton_debug_action import ImageButtonDebugAction
from virtualstudio2.plugins.debugaction.actions.rotary_encoder_debug_action import RotaryEncoderDebugAction


class DebugActionLauncher(ActionLauncher):

    def __init__(self):
        super(DebugActionLauncher, self).__init__()
        global PLUGIN_DIRECTORY
        PLUGIN_DIRECTORY = str(Path(__file__).resolve().parents[3])
        registerCategoryIcon(["Debug"], PLUGIN_DIRECTORY + "/assets/debug/icons/debug.png")

        self.ACTIONS = {
            CONTROL_TYPE_BUTTON: ButtonDebugAction,
            CONTROL_TYPE_FADER: FaderDebugAction,
            CONTROL_TYPE_IMAGE_BUTTON: ImageButtonDebugAction,
            CONTROL_TYPE_ROTARY_ENCODER: RotaryEncoderDebugAction
        }
    #region Metadata

    def getName(self):
        return "Debug Action (States)"

    def getIcon(self):
        return readPNGIcon(PLUGIN_DIRECTORY + "/assets/debug/icons/debug.png")

    def getCategory(self):
        return ["Debug"]

    def getAuthor(self):
        return "eric"

    def getVersion(self):
        return (0,0,1)

    def getActionStateCount(self, controlType: str) -> int:
        return len(controlType)

    def getActionUI(self, controlType: str) -> Tuple[str, str]:
        return UI_TYPE_INVALID, ""
    #endregion