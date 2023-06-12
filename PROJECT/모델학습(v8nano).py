from ultralytics import YOLO

model = YOLO("yolov8n.pt")
# Train the model using MPS as device
model.train(data='/Users/neo/Downloads/dataset/data.yaml', epochs=30, imgsz=416, optimizer='Adam', momentum=0.9, label_smoothing=0.1)
 