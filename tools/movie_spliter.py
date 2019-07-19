import cv2
vidcap = cv2.VideoCapture('./data2/mix1.mp4')
# x,y,w,h = 881,400,300,300   # merge
x,y,w,h = 823,477,200,350   # mix
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite("./data2/mix1/image"+str(count)+".jpg", image[y:y + h, x:x + w])     # save frame as JPG file
    return hasFrames
sec = 0
frameRate = 0.5 #//it will capture image in each 0.5 second
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)