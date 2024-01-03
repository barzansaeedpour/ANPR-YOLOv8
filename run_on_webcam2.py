from ultralytics import YOLO
# from ultralytics.yolo.v8.detect.predict import Dete


model = YOLO('./runs/detect/train21/weights/best.pt')
model.predict(source = '0', show = True, conf = 0.5)