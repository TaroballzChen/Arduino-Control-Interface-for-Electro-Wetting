from PyQt5.QtWidgets import QWidget,QLabel,QComboBox,QPushButton,QHBoxLayout

# Arduino Connect Fuction
from module.Arduino.Connect import Arduino_Connect


class Serial_block(QWidget,Arduino_Connect):
    def __init__(self,parent,statusbar):
        super(Serial_block, self).__init__()
        self.statusBar = statusbar
        self.setParent(parent)

    def init_UI(self):
        port_label = QLabel("Serial Port")
        self.port_combo = QComboBox()
        self.refresh_port_button = QPushButton("Refresh Ports")
        self.Arudino_connect_button = QPushButton("Connect")

        box = QHBoxLayout()
        box.addWidget(port_label)
        box.addWidget(self.port_combo)
        box.addWidget(self.refresh_port_button)
        box.addWidget(self.Arudino_connect_button)
        self.refresh_port_button.clicked.connect(self.GetCOMport)
        self.Arudino_connect_button.setCheckable(True)
        self.Arudino_connect_button.toggled.connect(self.Arduino_Connect)
        return box

    def Arduino_Connect(self):
        self.Arudino_connect_button.setEnabled(False)
        self.refresh_port_button.setEnabled(False)
        self.port_combo.setEnabled(False)
        self.Connected(self.port_combo.currentText())

    def GetCOMport(self):
        super(Serial_block, self).GetCOMport()
        self.port_combo.clear()
        self.port_combo.addItems(self.portlist)
