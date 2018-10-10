class LoadStatusBar():
    def __init__(self,statusbar):
        self.status = statusbar
        self.init_status()

    def init_status(self):
        self.status.showMessage("Arduino Disconnected")

    def Arduino_connected(self):
        self.status.showMessage("Arduino Connected")