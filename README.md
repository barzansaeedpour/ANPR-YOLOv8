# ANPR-YOLOv8
### Automatic number plate recognition (Iranian)

### سامانه تشخیص پلاک ایرانی

# Results

| image 1 | image 2 |
|----------|----------|
|<img src="files/1.jpg" alt="Image 1">|<img src="files/4.jpeg" alt="Image 4">|

# Dataset
You can download the dataset from my roboflow profile:
https://universe.roboflow.com/barzansaeedpour/anpr-iranian-2

You can also use the code in (download_dataset.py) to download it. 

# How to use
1- create a virtual environment:
```
python -m venv env
```
2- Activate it:
```
env\Scripts\activate
```

4- install ultralytics:
```
pip install ultralytics
```

5- install pytorch with cuda support:

```
pip install torch --upgrade torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

6- Train the model
```
yolo task=detect mode=train epochs=50 data='dataset/data.yaml' model=yolov8m.pt imgsz=300 batch=2 
```

7- Test the model
```
yolo task=detect mode=predict model="runs/detect/train/weights/best.pt" save=True conf=0.3 source='dataset/test/images/'
```

# Detection results (نمونه تشخیص)

|  |  |
|----------|----------|
|<img src="files/11.png" alt="Image 2">|<img src="files/11_detected_chars.png" alt="Image 3">|
|<img src="files/3_.png" alt="Image 2">|<img src="files/3_detected_chars.png" alt="Image 3">|

# Truck scale results (نمونه تشخیص در باسکول)

|  |  |
|----------|----------|
|<img src="files/2.png" alt="Image 2">|<img src="files/3.png" alt="Image 3">|
|<img src="files/5.png" alt="Image 5">|<img src="files/6.png" alt="Image 6">|
