from time import sleep

class Arduino_Control():
    def __init__(self):
        pass

    def into_detection(self,Arduino_object):
        cmd = 'a'.encode('utf-8')
        pause = '@'.encode("utf-8")
        self.SerialWrite(Arduino_object,cmd)
        self.SerialWrite(Arduino_object,pause)

    def into_collection(self,Arduino_object):
        cmd = 'b'.encode('utf-8')
        pause = '@'.encode("utf-8")
        self.SerialWrite(Arduino_object,cmd)
        self.SerialWrite(Arduino_object,pause)

    def into_waste(self,Arduino_object):
        cmd = 'c'.encode('utf-8')
        pause = '@'.encode("utf-8")
        self.SerialWrite(Arduino_object,cmd)
        self.SerialWrite(Arduino_object,pause)

    def SerialWrite(self,Arduino_object,command):
        Arduino_object.write(command)
        rv = Arduino_object.readline()
        Arduino_object.flushInput()