from virtualstudio.common.structs.action.button_action import ButtonAction


class RotaryEncoderDebugAction(ButtonAction):

    #region handlers

    def onLoad(self):
        print("OnLoad")

    def onAppear(self):
        print("OnAppear")

    def onDisappear(self):
        print("OnDisappear")

    def onSettingsGUIAppear(self):
        print("OnSettingsGUI Appear")

    def onSettingsGUIDisappear(self):
        print("OnSettingsGUI Disappear")

    def onParamsChanged(self, parameters: dict):
        print("Params Changed")

    #endregion

    # region Hardware Event Handlers

    def onKeyDown(self):
        print("On Key Down")
        print("parameters:", self.getParams())

    def onKeyUp(self):
        print("On Key Up")

    def onRotate(self, value: int):
        print("On Rotate, value=", value)

    # endregion