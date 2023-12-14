from ultralytics import YOLO
import cv2
import math 
import arabic_reshaper
from bidi.algorithm import get_display
from PIL import ImageFont, ImageDraw, Image
import numpy as np


# start webcam
cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)

# model
model = YOLO("./runs/detect/train19/weights/best.pt")

# classNames = [
#               'پلاک',
#               ]
classNames = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'be', 'dal', 'gaf', 'ghaf', 'h', 'he', 'jim', 'lam', 'mim', 'noon', 'sad', 'sin', 'ta', 'te', 'waw', 'ye']



def persian(text):
    # return get_display(arabic_reshaper.reshape(text))
    return text


while True:
    success, img = cap.read()
    results = model(img, stream=True)

    # coordinates
    for r in results:
        boxes = r.boxes

        for box in boxes:
            # bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

            # confidence
            confidence = math.ceil((box.conf[0]*100))/100
            print("Confidence --->", confidence)

            # class name
            cls = int(box.cls[0])
            print("Class name -->", classNames[cls])

            # object details
            org = [x1, y1-20]
            
            img = Image.fromarray(img)
            draw = ImageDraw.Draw(img)
            draw.rectangle([(x1, y1), (x2, y2)], outline ='red',)

            # font = ImageFont.truetype("./fonts/BZar.ttf", size=23)
            # font = ImageFont.truetype("./fonts/BZar.ttf", size=23)
            text = classNames[cls]
            color = (0, 0, 255)  # Red color
            draw.rectangle([(org[0], org[1]), (org[0]+(len(text)*15), org[1]+25)], fill =(255,100,100))
            # draw.text(org, persian(text), fill=(255,255,255), font=font)
            draw.text(org, persian(text), fill=(255,255,255))
            img = np.array(img)


    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()