from PyQt5.QtWidgets import QWidget,QLabel,QHBoxLayout,QVBoxLayout,QComboBox,QPushButton
from PyQt5.QtGui import QImage,QPixmap

#camera function
from module.camera.snapshot import Snapshot
from module.camera.CamLive import CameraLive

class camera(QWidget,Snapshot,CameraLive):
    def __init__(self,parent):
        super(camera, self).__init__()

        # camera live
        self.imgLabel = QLabel(self)
        self.imgLabel.setFixedWidth(480)
        self.imgLabel.setFixedWidth(640)
        self.button_Enable = False
        self.portlist = [str(x) for x in range(0, 11)]

        # snapshot
        self.snapLabel = QLabel(self)

        self.setParent(parent)

    def init_UI(self):
        camera_port_label = QLabel("camera Port")
        self.port_combo = QComboBox()
        self.port_combo.addItems(self.portlist)
        self.start_camera_button = QPushButton("Start Camera")
        self.start_camera_button.setCheckable(True)

        self.snapshot_button = QPushButton("SnapShot")


        camera_select_box = QHBoxLayout()
        camera_select_box.addWidget(camera_port_label)
        camera_select_box.addWidget(self.port_combo)
        camera_select_box.addWidget(self.start_camera_button)
        camera_select_box.addWidget(self.snapshot_button)
        self.start_camera_button.toggled.connect(self.start_camera)
        self.snapshot_button.clicked.connect(self.Start_Snapshot)

        Hbox = QHBoxLayout()
        Hbox.addWidget(self.imgLabel)
        Hbox.addWidget(self.snapLabel)

        box = QVBoxLayout()
        box.addLayout(Hbox)
        box.addLayout(camera_select_box)

        return box

    def start_camera(self):
        self.detect_webcam_Enabled(self.button_Enable)
        super(camera, self).start_camera()

    def detect_webcam_Enabled(self,status):
        if not status:
            self.button_Enable = True
            self.start_camera_button.setText("Stop camera")
        else:
            self.button_Enable = False
            self.start_camera_button.setText("Start Camera")

    def displayImage(self,img,window=1):
        qformat = QImage.Format_Indexed8
        try:
            if len(img.shape) ==3:     # shape 第0項為長 第一項為寬  第三項為channel RGB為3 灰階為1 RGBA含有透明度為4
                if img.shape[2] == 4:
                    qformat = QImage.Format_RGBA8888
                else:
                    qformat=QImage.Format_RGB888

            outImage = QImage(img,img.shape[1],img.shape[0],img.strides[0],qformat)
            outImage = outImage.rgbSwapped()

        except Exception:
            outImage = QImage(480,640,QImage.Format_RGB888)

        if window ==1:
            self.imgLabel.setPixmap(QPixmap.fromImage(outImage))
            self.imgLabel.setScaledContents(True)

        if window ==2:
            self.snapLabel.setPixmap(QPixmap.fromImage(outImage))
            self.snapLabel.setScaledContents(True)