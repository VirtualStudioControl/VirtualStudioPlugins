import sys

from config import PLUGIN_DIRECTORY
from virtualstudio.common.action_manager.actionmanager import registerCategoryIcon
from virtualstudio.common.structs.action.action_launcher import ActionLauncher, CONTROL_TYPE_BUTTON
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

    def getID(self):
        return "{}.{}.{}-{}".format(self.getAuthor(), self.getCategory(), self.getName(), self.getVersion())

    def allowedControls(self):
        return [CONTROL_TYPE_BUTTON]

    def getActionUI(self, control):
        return ""

    def getActionForControl(self, control):
        pass

    #endregion