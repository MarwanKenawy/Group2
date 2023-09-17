from Ultralytics import YOLO

model = YOLO(r"Model\best.pt")

model.predict(source="Model\WIN_20230917_14_23_29_Pro.jpg", classes=[0,1], show=True)