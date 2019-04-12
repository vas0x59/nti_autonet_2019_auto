from WebCam import WebCam
from RegLine import RegLine
from RegSvet import RegSvet
import time 
import cv2

# vs = WebCam(0)
# vs.start()

cap= cv2.VideoCapture(0)
# (self.grabbed, self.frame) = cap.read()
cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

rs = RegSvet(cap)

rs.load_model_nn("sv3.keras", "my_model_a.json")
rs.load_model_svm("tld.svm")


rs.reg_toggle(True)
rs.start()
# rs.update()
while True:
    print(rs.get_label())
    
    time.sleep(0.15)