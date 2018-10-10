from time import sleep
import serial
import glob
import sys

class Arduino_Connect():
    def __init__(self):
        self.portlist = []
        self.ser_obj = None

    def GetCOMport(self):
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')
        self.portlist.clear()
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                self.portlist.append(port)
            except (OSError, serial.SerialException):
                pass

    def Connected(self,serial_port):
        try:
            self.ser_obj = serial.Serial(serial_port, 9600, timeout=2)
            for i in range(1, 10):
                rv = self.ser_obj.readline()
                self.ser_obj.flushInput()
                sleep(0.1)  # Delay for one tenth of a secon
                Str = rv.decode("utf-8")
                # Debug print(Str[0:5])
                if Str[0:5] == "Ready":
                    break
            self.statusBar.Arduino_connected()

        except Exception:
            self.Arudino_connect_button.setEnabled(True)
            self.refresh_port_button.setEnabled(True)
            self.port_combo.setEnabled(True)