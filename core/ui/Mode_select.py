from PyQt5.QtWidgets import QWidget,QTabWidget,QHBoxLayout,QLabel,QLineEdit,QPushButton,QVBoxLayout


#Arduino Control Function
from module.Arduino.Control import Arduino_Control

class Mode(QWidget,Arduino_Control):
    def __init__(self,parent):
        super(Mode, self).__init__()
        self.setParent(parent)
        # self.arduino_obj = serial_object   # Arduino對象

    def init_UI(self):
        mode_tab = QTabWidget()
        mode_tab.setFixedWidth(250)
        mode_tab.addTab(self.Auto(),"Auto")
        mode_tab.addTab(self.Manual(),"Manual")
        box = QHBoxLayout()
        box.addWidget(mode_tab)

        return box

    def Auto(self):
        Auto_tab = QWidget()

        # Init UI
        Threshold_label = QLabel("Threshold")
        Threshold_input = QLineEdit()
        # run = QPushButton("Start")

        layout = QHBoxLayout()
        layout.addWidget(Threshold_label)
        layout.addWidget(Threshold_input)
        Auto_tab.setLayout(layout)


        return Auto_tab


    def Manual(self):
        manual_tab = QWidget()

        # Init UI
        self.into_detect_button = QPushButton("into detect")
        self.into_collection_button = QPushButton("into collection")
        self.into_waste_button = QPushButton("into waste")

        layout = QVBoxLayout()
        layout.addWidget(self.into_detect_button)
        layout.addWidget(self.into_collection_button)
        layout.addWidget(self.into_waste_button)
        manual_tab.setLayout(layout)

        return manual_tab