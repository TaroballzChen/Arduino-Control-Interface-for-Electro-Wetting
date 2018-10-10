from core.ui.Mode_select import Mode
from core.ui.serial_select import Serial_block
from core.ui.camera import camera
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QHBoxLayout

class BodyWindow(QWidget):
    def __init__(self,parent,statusBar):
        super(BodyWindow, self).__init__()
        self.setParent(parent)
        # Serialport_select
        serialport_select = Serial_block(self,statusBar)
        serial_widget = serialport_select.init_UI()


        # mode_select
        operate_mode_select = Mode(self)
        OperateMode_widget = operate_mode_select.init_UI()
        operate_mode_select.into_detect_button.clicked.connect(
            lambda: operate_mode_select.into_detection(serialport_select.ser_obj))
        operate_mode_select.into_collection_button.clicked.connect(
            lambda: operate_mode_select.into_collection(serialport_select.ser_obj))
        operate_mode_select.into_waste_button.clicked.connect(
            lambda: operate_mode_select.into_waste(serialport_select.ser_obj))

        # Camera_UI
        camera_ui = camera(self)
        camera_widget = camera_ui.init_UI()



        self.UI_Layout(camera_widget,
                       serial_widget,
                       OperateMode_widget)




    def UI_Layout(self,camera,*Widgets):
        select_block = QVBoxLayout()

        for w in Widgets:
            select_block.addLayout(w)
        else:
            UI_layout = QHBoxLayout()
            UI_layout.addLayout(select_block)
            UI_layout.addLayout(camera)
        self.setLayout(UI_layout)