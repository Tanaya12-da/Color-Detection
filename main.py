import cv2
from PIL import Image
from util import get_limits

yellow=[0,255,0]#green in bgr colorspace

cap=cv2.VideoCapture(0) # 0 for default webcam / 1 for second webcam
while True:
    ret,frame=cap.read()
    hsvImage=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lowerlimit, upperlimit=get_limits(color=green)

    mask=cv2.inRange(hsvImage,lowerlimit,upperlimit) 

    mask_=Image.fromarray(mask)
    #we create this mask_ so that we can create bounding box
    bbox=mask_.getbbox()
    if bbox is not None:
        x1,y1,x2,y2=bbox
        frame=cv2.rectangle(frame,(x1,y1) , (x2, y2), (0,255,0),5)

    # print(bbox) #getting none whwn there is no yellow color
   

    cv2.imshow('Frame',frame)
    if cv2.waitKey(1) &  0xFF == ord('q'): # waits until the 'q' key is pressed
        break

cap.release()

cv2.destroyAllWindows()
#in this we will be using hsv color space
