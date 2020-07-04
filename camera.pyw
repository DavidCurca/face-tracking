import numpy as np
import cv2
import time
import serial

ser = serial.Serial('COM4', 9800, timeout=10)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
cap = cv2.VideoCapture(0)
cicles = 0
ummm = 0
mx = 0
my = 0
mode = 1 #1 - nu pot incepe; 0 - scaneaza

def MouseEvents(event,x,y,flags,param):
    global mx
    global my
    global mode
    if event == cv2.EVENT_LBUTTONDOWN:
        mx, my = x, y;
        if(mx >= 5 and mx <= 150 and my >= 410 and my <= 470):
            print("BUTON APASAT");
            if(mode == 1):
                mode = 0
            else:
                mode = 1
    else:
        mx, my = 0, 0;

while 1:
    ret, img = cap.read()
    cv2.setMouseCallback('Face Traking Project', MouseEvents)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if(mode == 1):
        cv2.rectangle(img, (5, 410), (150, 470), (0, 255, 0), -1)
        cv2.putText(img,"START", (30,452), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)
    else:
        cv2.rectangle(img, (5, 410), (150, 470), (0, 0, 255), -1)
        cv2.putText(img,"STOP", (30,452), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)


    #------------ timp ------------
    now = time.localtime()
    cv2.putText(img,str((int)(now.tm_hour/10%10)) + str((int)(now.tm_hour%10)) + " : " + str((int)(now.tm_min/10%10)) + str((int)(now.tm_min%10)), (500,453), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
    
    #------------ titlu ------------
    cv2.putText(img,"E", (250,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
    cv2.putText(img,"P", (270,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,140,255), 2)
    cv2.putText(img,"I", (290,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)
    cv2.putText(img,"C", (300,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,252,124), 2)

    cv2.putText(img,"P", (340,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0), 2)
    cv2.putText(img,"R", (360,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
    cv2.putText(img,"O", (380,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (128,0,128), 2)
    cv2.putText(img,"J", (405,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
    cv2.putText(img,"E", (420,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,140,255), 2)
    cv2.putText(img,"C", (440,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)
    cv2.putText(img,"T", (460,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,252,124), 2)
    
    for (x,y,w,h) in faces:
        if(mode == 1):
            break;
        img_x = 'X: ' + str(x);
        img_y = 'Y: ' + str(y);
        motor_x = int((120 - (((x - 680) * (120 - 20) / (640 - 0) + 120)))) + 20;
        motor_y = int((150 - (((y - 480) * (150 - 50) / (480 - 0) + 150)))) + 50;
        s = str(motor_x) + " " + str(motor_y);
        #print(motor_x)
        res = ''.join(format(i, 'b') for i in bytearray(s, encoding ='utf-8'))
        if(cicles%5 == 0):
            ser.write(str.encode(s))
        cv2.putText(img,img_x, (20,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
        cv2.putText(img,img_y, (20,90), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        #------------ ochi ------------
        #eyes = eye_cascade.detectMultiScale(roi_gray)
        #for (ex,ey,ew,eh) in eyes:
        #    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        #    break;
        break; #decat prima fata
    
    cv2.imshow('Face Traking Project',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    if cv2.getWindowProperty('Face Traking Project',cv2.WND_PROP_AUTOSIZE) == -1:        
        break
    time.sleep(0.01)
    cicles += 1
    #if(mx != 0 and my != 0):
        #print(mx, my)

cap.release()
cv2.destroyAllWindows()
exit(0)
