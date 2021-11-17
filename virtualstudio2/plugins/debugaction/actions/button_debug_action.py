from virtualstudio.common.logging import logengine
from virtualstudio.common.structs.action.button_action import ButtonAction


logger = logengine.getLogger()

class ButtonDebugAction(ButtonAction):

    #region handlers

    def onLoad(self):
        logger.info("OnLoad")

    def onAppear(self):
        logger.info("OnAppear")

    def onDisappear(self):
        logger.info("OnDisappear")

    def onSettingsGUIAppear(self):
        logger.info("OnSettingsGUI Appear")

    def onSettingsGUIDisappear(self):
        logger.info("OnSettingsGUI Disappear")

    def onParamsChanged(self, parameters: dict):
        logger.info("Params Changed")

    #endregion

    #region Hardware Event Handlers

    def onKeyDown(self):
        logger.info("OnKeyDown")

    def onKeyUp(self):
        logger.info("OnKeyUp")
        self.nextState()

    #endregion