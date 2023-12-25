import cv2
import os

for N in [2,3,4,5,6,7,8]:
    video_path= f'./dataset/videos/tehran_0{N}.mp4'
    vidcap = cv2.VideoCapture(video_path)
    success,image = vidcap.read()
    count = 0
    target_path = f"./dataset/tehran/"
    os.makedirs(target_path, exist_ok=True)

    # fps = 30
    while success:
        
        if count==0 or count % 5 == 0:
            cv2.imwrite(f"{target_path}/frame-{N}-{count:07d}.jpg" , image)     # save frame as JPEG file      
        
        success,image = vidcap.read()
        # print('Read a new frame: ', success)
        count += 1
