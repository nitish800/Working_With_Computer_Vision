import numpy as np
import cv2


cap= cv2.VideoCapture(0) # using 0 for choosing first camera, 1 for second and so on

while(True):
    # Capture frame-by-frame, since video is a secequence of image
    ret, frame = cap.read()

    #opertion: changing the color of frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #display the resulting frame

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


#when every thing is done
cap.release()
cv2.DestroyAllWindows()
