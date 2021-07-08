import sys
from typing import Tuple

from config import PLUGIN_DIRECTORY
from virtualstudio.common.action_manager.actionmanager import registerCategoryIcon
from virtualstudio.common.io import filewriter
from virtualstudio.common.structs.action.action_launcher import ActionLauncher, CONTROL_TYPE_BUTTON, UI_TYPE_INVALID, \
    UI_TYPE_QTUI
from virtualstudio.common.tools import icontools
from virtualstudio.common.tools.icontools import readPNGIcon


class DebugActionLauncher(ActionLauncher):

    def __init__(self):
        super(DebugActionLauncher, self).__init__()
        registerCategoryIcon(["Debug"], PLUGIN_DIRECTORY + "/assets/debug/icons/debug.png")

    #region Metadata

    def getName(self):
        return "Debug Action (Button)"

    def getIcon(self):
        return readPNGIcon(PLUGIN_DIRECTORY + "/assets/debug/icons/debug.png")

    def getCategory(self):
        return ["Debug"]

    def getAuthor(self):
        return "eric"

    def getVersion(self):
        return (0,0,1)

    def allowedControls(self):
        return [CONTROL_TYPE_BUTTON]

    def getActionStateCount(self, controlType: str) -> int:
        return 1

    def getActionUI(self, controlType: str) -> Tuple[str, str]:
        return UI_TYPE_QTUI, \
               icontools.encodeIconData(
                   filewriter.readFileBinary(PLUGIN_DIRECTORY + "/assets/debug/widgets/debugwidget1.ui"))

    def getActionForControl(self, control):
        pass

    #endregion