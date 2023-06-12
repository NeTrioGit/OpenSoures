from ultralytics import YOLO

# Load the model from last.pt
model =YOLO("/opt/homebrew/runs/detect/train17/weights/last.pt") 

# Train the model using MPS as device
model.train(data='/Users/neo/Downloads/dataset/data.yaml', epochs=30, imgsz=416, optimizer='Adam', momentum=0.9, label_smoothing=0.1)
