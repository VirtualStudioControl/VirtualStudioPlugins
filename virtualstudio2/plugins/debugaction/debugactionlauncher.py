import sys

from virtualstudio.common.action_manager.actionmanager import registerCategoryIcon
from virtualstudio.common.account_manager.account_manager import registerAccountType
from virtualstudio.common.io import filewriter
from virtualstudio.common.structs.action.action_launcher import *
from virtualstudio.common.tools import icontools
from virtualstudio.common.tools.icontools import readPNGIcon
from virtualstudio2.plugins.debugaction.actions.button_debug_action import ButtonDebugAction
from virtualstudio2.plugins.debugaction.actions.fader_debug_action import FaderDebugAction
from virtualstudio2.plugins.debugaction.actions.imagebutton_debug_action import ImageButtonDebugAction
from virtualstudio2.plugins.debugaction.actions.rotary_encoder_debug_action import RotaryEncoderDebugAction

from pathlib import Path

class DebugActionLauncher(ActionLauncher):

    def __init__(self):
        global PLUGIN_DIRECTORY
        PLUGIN_DIRECTORY = str(Path(__file__).resolve().parents[3])

        super(DebugActionLauncher, self).__init__()
        registerCategoryIcon(["Debug"], PLUGIN_DIRECTORY + "/assets/debug/icons/debug.png")
        registerAccountType("Debugging Account", PLUGIN_DIRECTORY + "/assets/debug/icons/debug.png")

        self.ACTIONS = {
            CONTROL_TYPE_BUTTON: ButtonDebugAction,
            CONTROL_TYPE_FADER: FaderDebugAction,
            CONTROL_TYPE_IMAGE_BUTTON: ImageButtonDebugAction,
            CONTROL_TYPE_ROTARY_ENCODER: RotaryEncoderDebugAction
        }

    #region Metadata

    def getName(self):
        return "Debug Action"

    def getIcon(self):
        return readPNGIcon(PLUGIN_DIRECTORY + "/assets/debug/icons/debug.png")

    def getCategory(self):
        return ["Debug"]

    def getAuthor(self):
        return "eric"

    def getVersion(self):
        return (0,0,1)

    def getActionStateCount(self, controlType: str) -> int:
        return 1

    def getActionUI(self, controlType: str) -> Tuple[str, str]:
        return UI_TYPE_QTUI, \
               icontools.encodeIconData(
                   filewriter.readFileBinary(PLUGIN_DIRECTORY + "/assets/debug/widgets/debugwidget1.ui"))
    #endregion