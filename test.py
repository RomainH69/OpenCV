import cv2
import numpy as np

cap=cv2.VideoCapture(2)
ret, ref=cap.read()

while True:
    ret, frame=cap.read()
    #cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

    elif cv2.waitKey(1) & 0xFF==ord('c'):
        img_ref="opencv_reference_frame.png"
        cv2.imwrite(img_ref, frame)
        ref=frame

    current=frame

    delta=cv2.absdiff(current, ref)

    thresh=cv2.threshold(delta, 25, 255, cv2.THRESH_BINARY)[1]
    thresh=cv2.dilate(thresh, None, iterations=2)


    cv2.imshow('diff', thresh)

cap.release()
cv2.destroyAllWindows()
