import sys
from typing import Tuple

from virtualstudio.common.action_manager.actionmanager import registerCategoryIcon
from virtualstudio.common.io import filewriter
from virtualstudio.common.structs.action.action_launcher import ActionLauncher, CONTROL_TYPE_BUTTON, UI_TYPE_INVALID, \
    UI_TYPE_QTUI
from virtualstudio.common.tools import icontools
from virtualstudio.common.tools.icontools import readPNGIcon
from virtualstudio.plugins.debugaction.actions.button_debug_action import ButtonDebugAction

from pathlib import Path

class DebugActionLauncher(ActionLauncher):

    def __init__(self):
        global PLUGIN_DIRECTORY
        PLUGIN_DIRECTORY = str(Path(__file__).resolve().parents[3])

        super(DebugActionLauncher, self).__init__()
        registerCategoryIcon(["Debug"], PLUGIN_DIRECTORY + "/assets/debug/icons/debug.png")

        self.ACTIONS = {
            CONTROL_TYPE_BUTTON: ButtonDebugAction
        }
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

    def getActionStateCount(self, controlType: str) -> int:
        return 1

    def getActionUI(self, controlType: str) -> Tuple[str, str]:
        return UI_TYPE_QTUI, \
               icontools.encodeIconData(
                   filewriter.readFileBinary(PLUGIN_DIRECTORY + "/assets/debug/widgets/debugwidget1.ui"))
    #endregion