#this is a pushup counter
import cv2
import numpy as np
import poseModule as pm


cap=cv2.VideoCapture(r'open_cv\pushup counter\istock-578758310_preview.mp4')

detector=pm.poseDetector()
count=0
direction=0


while True:
    #image preprocessing
    success,image=cap.read()
    image=cv2.resize(image,(1000,480))

    #find body
    image=detector.findPose(image,draw=False)
    #print(image)
    lmlist=detector.findPosition(image,draw=False)
    #print(lmlist)

    #find angles of specific landmarks

    if len(lmlist)!=0:
        #angle=detector.findAngle(image,12,14,16)#1 leg
        #print(angle)
        angle=detector.findAngle(image,11,13,15)# nxt leg
        print(angle)

    #counting
    #converting angle from 0 to 180 to 0 to100
    percentage=np.interp(angle,(200,250),(0,100))# interp-to convert degree to value
    #print(percentage)
    if percentage==100:# standing
        if direction==0:# dowm
            count=count+0.5
            direction=1
    if percentage==0:# dowm
        if direction==1:
            count=count+0.5
            direction=0
    #print(count)
    cv2.rectangle(image,(0,0),(150,150),(0,0,0),cv2.FILLED)
    cv2.putText(image,str(int(count)),(50,100),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),5)


    
    

    cv2.putText(image,str(int(percentage)),(800,100),cv2.FONT_HERSHEY_COMPLEX,3,(0,255,0),3)








    
    cv2.imshow('pushup counter',image)
    if cv2.waitKey(1)&0xFF==27:
        break
