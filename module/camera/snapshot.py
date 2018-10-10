import cv2

class Snapshot():
    def __init__(self):
        self.snapshot = None
    def Start_Snapshot(self):
        if self.button_Enable:
            try:
                photo = cv2.cvtColor(self.image.copy(),cv2.COLOR_BGR2BGRA)
                photo = cv2.GaussianBlur(photo,(21,21),0)
                self.snapshot = photo
                self.displayImage(self.snapshot,2)
            except Exception:
                pass