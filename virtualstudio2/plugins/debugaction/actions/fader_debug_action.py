from virtualstudio.common.logging import logengine
from virtualstudio.common.structs.action.fader_action import FaderAction

logger = logengine.getLogger()

class FaderDebugAction(FaderAction):

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

    # region Hardware Event Handlers

    def onTouchStart(self):
        logger.info("onTouchStart")
        logger.info("parameters:", self.getParams())

    def onTouchEnd(self):
        logger.info("onTouchEnd")

    def onMove(self, value):
        logger.info("onMove, value: ", value)

    # endregion