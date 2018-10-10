from time import sleep
import serial
from getch import getch
import serial.tools.list_ports
import glob
import sys


def get_comports():
    plist = list(serial.tools.list_ports.comports())
    if len(plist) <= 0:
        print("The Serial port can't find!")
    else:
        try:
            for port in plist:
                serialName = port[0]
                serialFd = serial.Serial(serialName, 9600, timeout=60)
                print("check which port was really used >", serialFd.name)
        except Exception as e:
            pass


if __name__ == '__main__':
    get_comports()
    ##==============================================================================
    ser = serial.Serial("/dev/cu.usbmodem1421", 9600, timeout=2)  # Establish the connection on a specific port


    ##==============================================================================

    ##=======getchar========================
    def getchar():
        # Returns a single character from standard input
        key = getch()  ##Get byte         ex: b'a'
        key_num = ord(key)  ##convert byte to integer    97
        key_chr = chr(key_num)  ##convert integer to char       'a'
        return key_num


    ##====================================

    ##======Write Serial Command to arduino============
    def SerialWrite(command):
        ser.write(command)
        rv = ser.readline()
        # print (rv) # Read the newest output from the Arduino
        print(rv.decode("utf-8"))
        sleep(1)  # Delay for one tenth of a second
        ser.flushInput()


    ##====================================

    ##=======Get  Ready================
    print("Connecting to Arduino.....")
    for i in range(1, 10):
        rv = ser.readline()
        print("Loading...")
        # Debug print (rv) # Read the newest output from the Arduino
        print(rv.decode("utf-8"))
        ser.flushInput()
        sleep(1)  # Delay for one tenth of a secon
        Str = rv.decode("utf-8")
        # Debug print(Str[0:5])
        if Str[0:5] == "Ready":
            print("Get Arduino Ready !")
            break
    ##------------------------------------------------------

    print("==================================")
    ##counter = 65  # "A"
    ##ser.write(chr(counter).encode('utf-8')) # Convert the decimal number to ASCII then send it to the Arduino
    # cmd = "Key in the Command".encode("utf-8")
    # SerialWrite(cmd)

    ##===Get char from keyboard then send to arduino and get it back to print in screen==
    while True:
        chr_num = getchar()
        if chr_num  < 95 or chr_num > 122:
            continue
        cmd = (chr(chr_num).encode('utf-8'))
        SerialWrite(cmd)
        if chr_num == 27:  ##ESC
            break
    ser.close()


