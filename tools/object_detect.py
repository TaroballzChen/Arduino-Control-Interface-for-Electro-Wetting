import numpy as np
import cv2
import time
import matplotlib.pyplot as plt

cap = cv2.VideoCapture("./data2/merge1.mp4")
# x, y, w, h = 210, 635, 190, 90
#x,y,w,h = 176,498,170,90

# x,y,w,h = 823,477,200,350   # mix
x,y,w,h = 881,400,300,300   # merge

start = time.time()
AREA = np.ndarray([])
r_channel = np.ndarray([])
g_channel = np.ndarray([])
b_channel = np.ndarray([])
timelist = np.chararray([])

while cap.isOpened():
    ret , frame =  cap.read()
    if ret == False:
        break
    frame = frame[y:y + h, x:x + w]

    blurred_frame = cv2.GaussianBlur(frame,(7,7),0)

    hsv  = cv2.cvtColor(blurred_frame,cv2.COLOR_BGR2HSV)

    lower_red = np.array([0,70,70])
    upper_red = np.array([255,255,255])
    mask = cv2.inRange(hsv,lower_red,upper_red)

    contours, _ =  cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    if not contours:
        AREA = np.append(AREA, 0)
        r_channel = np.append(r_channel, 0)
        g_channel = np.append(g_channel, 0)
        b_channel = np.append(b_channel,0)


    for contour in contours:
        area = cv2.contourArea(contour)

        (x_,y_),radius = cv2.minEnclosingCircle(contour)
        center = (int(x_),int(y_))
        center_ = (int(y_),int(x_))
        # radius = int(radius)
        # frame = cv2.circle(frame,center,radius,(0,0,255,),2)
        r,g,b = cv2.split(frame)
        # print(r[center_],g[center_],b[center_])

        AREA = np.append(AREA, area)
        r_channel = np.append(r_channel, r[center_])
        g_channel = np.append(g_channel, g[center_])
        b_channel = np.append(b_channel, b[center_])


        if area > 1:
            cv2.drawContours(frame, contour, -1, (0, 255, 0), 1)




    elpase = time.time() - start

    cv2.namedWindow("Mask",0)
    cv2.resizeWindow("Mask",400,400)
    cv2.putText(mask,"%.3f"%elpase,(10,339),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255),1)
    cv2.imshow("Mask",mask)
    cv2.moveWindow("Mask",100,100)

    cv2.namedWindow("Frame",0)
    cv2.putText(frame, "%.3f,area=%d" %(elpase,AREA[-1]), (10, 339), cv2.FONT_HERSHEY_COMPLEX, 0.4, (255, 0, 255), 1)
    cv2.imshow("Frame",frame)
    cv2.resizeWindow("Frame",400,400)
    cv2.moveWindow("Frame", 500, 100)

    key = cv2.waitKey(15) & 0XFF == ord("q")
    if key == 27:
        break


plt.figure()
plt.subplot(411)
plt.plot(AREA,color="k")
plt.ylabel("Area(pixel)")

plt.subplot(412)
plt.plot(r_channel,color="r")
plt.ylabel("red_chan")


plt.subplot(413)
plt.plot(g_channel,color="g")
plt.ylabel("green_chan")

plt.subplot(414)
plt.plot(b_channel,color="b")
plt.ylabel("blue_chan")
plt.xlabel("frame")



# plt.plot(AREA,color="k")
# plt.ylabel("Area(pixel)")
# plt.xlabel("frame")
plt.show()

cap.release()
cv2.destroyAllWindows()