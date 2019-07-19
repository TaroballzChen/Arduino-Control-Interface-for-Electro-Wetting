import cv2
import numpy as np


cap = cv2.VideoCapture("./data/movie1.mp4")
fgbg = cv2.createBackgroundSubtractorKNN()

x, y, w, h = 210, 635, 190, 90
ret, frame1 = cap.read()
frame1 = frame1[y:y + h, x:x + w]
ret, frame2 = cap.read()
frame2 = frame2[y:y + h, x:x + w]

flag = False


while flag == False:
    flag = False
    gray_1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    gray_2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    blur_1 = cv2.GaussianBlur(gray_1,(5,5),0)
    blur_2 = cv2.GaussianBlur(gray_2,(7,7),0)


    diff = cv2.absdiff(blur_1,blur_2)
    # gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)

    # blur = cv2.GaussianBlur(gray,(5,5),0)
    _, thresh = cv2.threshold(diff,20,255,cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh,None,iterations=3)
    contours, _ = cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        x_,y_,w_,h_ = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 200:
            continue

        cv2.rectangle(frame1,(x_,y_),(x_+w_,y_+h_),(0,255,0),1)




    # cv2.drawContours(frame1,contours, -1, (0,255,0),1)
    cv2.imshow("original",frame1)
    frame1 = frame2

    # while time.time() - start < 0.1:
    ret,frame2 = cap.read()
    if ret == False:
        flag = True
            # break
    frame2 = frame2[y:y + h, x:x + w]
    # else:
    #     start = time.time()


    # ret, frame = cap.read()
    # x,y,w,h = 210,635,190,90
    # frame1 = frame1[y:y+h, x:x+w]
    # fgmask = fgbg.apply(frame)
    #
    # b,g,r = cv2.split(frame)
    #
    # cv2.imshow("original",frame1)
    # cv2.imshow("fg",fgmask)
    # cv2.imshow("Blue",b)
    # cv2.imshow("Green",g)
    # cv2.imshow("Red",r)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break


cap.release()
cv2.destroyAllWindows()