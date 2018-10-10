from PyQt5.QtCore import QTimer
import cv2

class CameraLive():
    def __init__(self):
        self.image = None

    def start_camera(self):
        if self.button_Enable:
            self.capture = cv2.VideoCapture(self.port_combo.currentIndex())               # 指定要使用那一隻攝影機
            self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
            self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,640)
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.update_frame)
            self.timer.start(5)
        else:
            self.stop_camera()

    def stop_camera(self):
        self.timer.stop()
        self.capture.release()
        cv2.destroyAllWindows()

    def update_frame(self):
        ret,self.image = self.capture.read()
        self.image = cv2.flip(self.image,1)              # Flipped Horizontally 水平翻转
        self.displayImage(self.image,1)

