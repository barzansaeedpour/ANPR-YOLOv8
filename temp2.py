from ultralytics import YOLO
import cv2
from math import sqrt, atan, degrees
import math 
import arabic_reshaper
from bidi.algorithm import get_display
from PIL import ImageFont, ImageDraw, Image
import numpy as np


def find_longest_line(plate_img, plate_img_gr):
    kernel_size = 3
    blur_gray = cv2.GaussianBlur(plate_img_gr, (kernel_size, kernel_size), 0)

    low_threshold = 150
    high_threshold = 200

    edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

    rho = 1  # distance resolution in pixels of the Hough grid
    theta = np.pi / 180  # angular resolution in radians of the Hough grid
    threshold = 15  # minimum number of votes (intersections in Hough grid cell)
    min_line_length = 50  # minimum number of pixels making up a line
    max_line_gap = 5  # maximum gap in pixels between connectable line segments
    line_image = np.copy(plate_img) * 0  # creating a blank to draw lines on

    # Run Hough on edge detected image
    # Output "lines" is an array containing endpoints of detected line segments
    lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]),
                        min_line_length, max_line_gap)

    lls = []
    for indx, line in enumerate(lines):
        for x1,y1,x2,y2 in line:
            cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),5)
            line_length = sqrt((x2-x1)**2 + (y2-y1)**2)
            lls.append((indx,line_length))
    lls.sort(key = lambda x: x[1])
    linessorted = []
    for (indx,ll) in lls:
        linessorted.append(lines[indx])
    return linessorted

def find_line_angle(line):
    x1,y1,x2,y2 = line[0]
    angle = degrees(atan(((y2-y1)/(x2-x1))))
    return angle

def rotate_image(plate_img_gr, angle):
    (h, w) = plate_img_gr.shape
    (cX, cY) = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
    rotated = cv2.warpAffine(plate_img_gr, M, (w, h))
    return rotated

def adjust_cropping(rotated_img):
    h,w = rotated_img.shape
    targ_h = int(w/4)
    crop_h = int((h - targ_h)/2)
    cropped_rotated_img = rotated_img[crop_h:h-crop_h,:]
    return cropped_rotated_img

def adjust(plate_img):    
    linessorted = find_longest_line(plate_img, plate_img[:,:,0])
    rot_angle = find_line_angle(linessorted[-1])
    rotated_img = rotate_image(plate_img[:,:,0], rot_angle)
    cropped_rotated_img = adjust_cropping(rotated_img)
    cw = cropped_rotated_img.shape[1]
    cv2.imwrite('results/adjusted_cropped_image.png', cropped_rotated_img)
    return cropped_rotated_img
# Draw the lines on the  image
#lines_edges = cv.addWeighted(plate_img, 0.8, line_image, 1, 0)

# # start webcam
# cap = cv2.VideoCapture(0)
# cap.set(3, 640)
# cap.set(4, 480)

# model
model = YOLO("./runs/detect/train/weights/best.pt")

classNames = [
              'پلاک',
              ]

# def crop(image, coord):
#             cropped_image = image[int(coord[1]):int(coord[3]), int(coord[0]):int(coord[2])]
#             return cropped_image

def persian(text):
    return get_display(arabic_reshaper.reshape(text))

# image_path = './dataset/yolov8/test/images/100_jpg.rf.98eed42565c91e604d2c2ee7f558792a.jpg'
# image_path = 'dataset/yolov8/test2/r2-7ea5-41789-11130-3.jpg'
# image_path = 'dataset/yolov8/test2/WhatsApp Image 2022-05-30 at 9.52.11 PM (1).jpeg'
# image_path = 'dataset/yolov8/test2/1652275461010_shot.jpg'
# image_path = 'dataset/yolov8/test2/kapra.jpg'
# image_path = 'dataset/yolov8/test2/Screenshot 2022-06-07 094350.png'
image_path = 'dataset/yolov8/test2/Screenshot 2022-06-07 102750.png'



img = cv2.imread(image_path)
# results = model(img, stream=True)
results = model.predict(source=image_path, conf = 0.1, show = False) 



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
        
        cropped_image = img[y1:y2, x1:x2]
        cv2.imwrite('results/cropped_image.png', cropped_image)


        # plate_img = cv.imread(os.path.join(plates_folder, "plate_4.jpg"))
        plate_img = cropped_image
        # plate_img_gr = cv2.imread('results/cropped_image.png', 0 )


        # try:
        #     plate_img = adjust(plate_img)
        # except:
        #     pass

        h = plate_img.shape[0]
        w = plate_img.shape[1]

        chopfactors = [(40,120),(100,200),(180,280),(270,360),(350,400),(400,460),(460,530),(530,600)]
        plate_letters= []
        for i, factor in enumerate(chopfactors):
            w1 = int((factor[0]/600)*w)
            w2 = int((factor[1]/600)*w)
            letterpatch = plate_img[:,w1:w2]
            #cv.imwrite(f"{str(factor[0])}_{str(factor[1])}.png", letterpatch)
            letterpatch_resized = cv2.resize(letterpatch, (28,28), interpolation= cv2.INTER_LINEAR)
            cv2.imwrite(f'results/{i}.png', letterpatch_resized)
            plate_letters.append(letterpatch_resized)

        img = Image.fromarray(img)
        draw = ImageDraw.Draw(img)
        draw.rectangle([(x1, y1), (x2, y2)], outline ='red',)

        font = ImageFont.truetype("./fonts/BZar.ttf", size=23)
        text = classNames[cls]
        color = (0, 0, 255)  # Red color
        padding_right = len(persian(text)) * 20
        draw.rectangle([(org[0], org[1]), (org[0]+padding_right, org[1]+25)], fill =(255,100,100))
        draw.text(org, persian(text), fill=(255,255,255), font=font)
        img = np.array(img)


    cv2.imwrite('results/r.png', img)