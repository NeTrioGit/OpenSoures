from ultralytics import YOLO


model =YOLO("/opt/homebrew/runs/detect/train2/weights/best.pt") # 학습된 모델 불러오기

# inputs = [img, img]  # list of numpy arrays
# results = model(inputs, stream=True)  # generator of Results objects


# Track with the model
# results = model.track(source="https://youtu.be/Zgi9g1ksQHc", show=True) 
results = model.track(source="https://youtu.be/A90y7secV5c", show=True, tracker="botsort.yaml") 

for result in results:
    boxes = result.boxes  # Boxes object for bbox outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    probs = result.probs  # Class probabilities for classification outputs


# model.predict(source, save=True, imgsz=320, conf=0.5)
