# ANPR-YOLOv8

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
pip install --upgrade torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116
```
<!-- pip install torch --upgrade torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118 -->

6- Train the model
```
yolo task=detect mode=train epochs=5 data='dataset\yolov8\data.yaml' model=yolov8m.pt imgsz=300 batch=2 
```