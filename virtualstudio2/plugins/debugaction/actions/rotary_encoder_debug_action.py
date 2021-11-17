from virtualstudio.common.logging import logengine
from virtualstudio.common.structs.action.rotary_encoder_action import RotaryEncoderAction

logger = logengine.getLogger()


class RotaryEncoderDebugAction(RotaryEncoderAction):

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

    def onKeyDown(self):
        logger.info("On Key Down")

    def onKeyUp(self):
        logger.info("On Key Up")

    def onRotate(self, value: int):
        logger.info("On Rotate, value=", value)

    # endregion