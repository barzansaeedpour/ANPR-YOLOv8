from ultralytics import YOLO


Number = 15
model = YOLO(f"./runs/detect/train{Number}/weights/best.pt")
# model.predict(source='dataset/Khanm-Rahmani/selected_mini/', conf = 0.4, save=True, show = False, save_txt = True) 
model.predict(source='dataset/char3/test/images', conf = 0.10, save=True, show = False, save_txt = True) 
  