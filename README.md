# ANPR-YOLOv8
### Automtic number plate recognition (Iranian)

### سامانه هوشمند تشخیص پلاک ایرانی

# Results

| image 1 | image 2 |
|----------|----------|
|<img src="files/1.jpg" alt="Image 1">|<img src="files/4.jpeg" alt="Image 4">|



# How to use:
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
yolo task=detect mode=train epochs=50 data='dataset\yolov8\data.yaml' model=yolov8m.pt imgsz=300 batch=2 
```

7- Test the model
```
yolo task=detect mode=predict model="runs/detect/train/weights/best.pt" save=True conf=0.3 source='dataset/yolov8/test/images/'
```