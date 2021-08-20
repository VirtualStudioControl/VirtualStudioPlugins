from virtualstudio.common.structs.action.button_action import ButtonAction


class FaderDebugAction(ButtonAction):

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

    def onTouchStart(self):
        print("onTouchStart")
        print("parameters:", self.getParams())

    def onTouchEnd(self):
        print("onTouchEnd")

    def onMove(self, value):
        print("onMove, value: ", value)

    # endregion