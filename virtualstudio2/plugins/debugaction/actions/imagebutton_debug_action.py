from virtualstudio.common.logging import logengine
from virtualstudio.common.structs.action.imagebutton_action import ImageButtonAction

logger = logengine.getLogger()


class ImageButtonDebugAction(ImageButtonAction):

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
        self.nextState()

    def onKeyUp(self):
        logger.info("OnKeyUp")

    #endregion