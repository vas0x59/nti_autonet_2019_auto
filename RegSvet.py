import numpy as np
import cv2
import cv2 as cv
from keras.preprocessing.image import img_to_array
from keras.models import load_model
from keras import backend as K
# model = load_model('sv3.keras')
# from tensorflow.keras.models import model_from_json
import dlib
from threading import Thread

class RegSvet:
    def __init__(self, vs):
        self.labels = ['red', 'yellow', 'green']
        self.label = "none"
        self.vs = vs
        self.reg_t = False
        self.stop_t = False
        
    def load_model_nn(self, w, j):
        # f = open(j, 'r')
        # json_string = f.readline()
        # f.close()
        # self.model = model_from_json(json_string)
        # self.model.load_weights(w)
        pass
        
    def load_model_svm(self, p):
        self.model_detector = dlib.simple_object_detector("tld.svm")

    def predict_label(self, inm):
        image = inm.copy()
        image = cv2.resize(image, (38, 38))
        # image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        cv2.imshow("image", image)
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)
        image = np.array(image, dtype="float") / 255.0
        # print(image)
        pre = self.model.predict(image)[0]
        # K.clear_session()
        i_max = 0
        for i in range(len(pre)):
            if pre[i_max] < pre[i]:
                i_max = i
        return self.labels[i_max]
    
    def reg_svet(self, frame):
        boxes = self.model_detector(frame)
        label = "none"
        for box in boxes:
            print (box)
            (x, y, xb, yb) = [box.left(), box.top(), box.right(), box.bottom()]
            if x > 0 and y > 0 and xb > 0 and yb > 0:
                crop = frame[y:yb, x:xb].copy()
                label = self.predict_label(crop)
        return label

    def reg_toggle(self, q):
        self.reg_t = q
    def stop(self):
        self.stop_t = True
    def update(self):
        self.model = load_model("sv3.keras")
        while not self.stop_t:
            frame = self.vs.read()
            # print(frame)
            cv2.imshow("frame", frame)
            cv2.waitKey(1)
            if self.stop_t:
                break
            self.label = self.reg_svet(frame)
            
            
    def get_label(self):
        return self.label
    def start(self):

        t = Thread(target=self.update, args=())
        t.daemon = True
        t.start()
