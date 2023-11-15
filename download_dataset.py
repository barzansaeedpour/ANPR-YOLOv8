
# first you need to install roboflow:
#### pip install roboflow

# download the dataset

from roboflow import Roboflow
rf = Roboflow(api_key="YOUR-API-KEY")
project = rf.workspace("barzansaeedpour").project("anpr-iranian-2")
dataset = project.version(2).download("yolov8")

