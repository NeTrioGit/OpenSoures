import cv2
from ultralytics import YOLO

cap = cv2.VideoCapture("/Users/neo/Downloads/[AW2] 후방 영상.mp4") # 실행 시키고자 하는 영상 불러오기
model =YOLO("/opt/homebrew/runs/detect/train2/weights/best.pt") # 학습된 모델 불러오기
while True:
    ret, frame = cap.read()
    if not ret:
        break
    results = model.track(frame, persist=True)
    boxes = results[0].boxes.xyxy.cpu().numpy().astype(int)
    ids = results[0].boxes.id.cpu().numpy().astype(int)
    for box, id in zip(boxes, ids):
        cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)
        cv2.putText(
        frame,
        f"Id {id}",
        (box[0], box[1]),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2,
    )
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break