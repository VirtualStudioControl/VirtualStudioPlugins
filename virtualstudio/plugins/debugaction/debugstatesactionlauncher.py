import sys

from config import PLUGIN_DIRECTORY
from virtualstudio.common.action_manager.actionmanager import registerCategoryIcon
from virtualstudio.common.structs.action.action_launcher import *
from virtualstudio.common.tools.icontools import readPNGIcon

class DebugActionLauncher(ActionLauncher):

    def __init__(self):
        super(DebugActionLauncher, self).__init__()
        registerCategoryIcon(["Debug"], PLUGIN_DIRECTORY + "/assets/debug/icons/debug.png")

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

    def allowedControls(self):
        return [CONTROL_TYPE_BUTTON, CONTROL_TYPE_IMAGE_BUTTON, CONTROL_TYPE_ROTARY_ENCODER, CONTROL_TYPE_FADER]

    def getActionStateCount(self, controlType: str) -> int:
        return len(controlType)

    def getActionUI(self, controlType: str) -> Tuple[str, str]:
        return UI_TYPE_INVALID, ""

    def getActionForControl(self, control):
        pass

    #endregion