from WebCam import WebCam
from RegLine import RegLine
from RegSvet import RegSvet
import time 

vs = WebCam(1)
vs.start()

rs = RegSvet(vs)

rs.load_model_nn("sv3.keras", "my_model_a.json")
rs.load_model_svm("tld.svm")

rs.start()
rs.reg_toggle(True)


while True:
    print(rs.get_label())
    time.sleep(0.5)