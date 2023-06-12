import cv2
from ultralytics import YOLO

cap = cv2.VideoCapture("/Users/neo/Downloads/dataset/성산대교 남단에서 올림픽대로까지 후방 영상 [Lukas H900].mp4")
model = YOLO("/opt/homebrew/runs/detect/train2/weights/best.pt")

# 출력 파일 설정
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # ("XVID") 와 동일
output_filename = "output.avi"
out = cv2.VideoWriter(output_filename, fourcc, fps, (width, height))

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
            0.5,  # 글자 크기 변경 (기본 값: 1)
            (0, 0, 255),
            2,
        )

    # 출력 파일에 프레임 저장
    out.write(frame)

    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# 자원 해제
cap.release()
out.release()  # 출력 파일 닫기
cv2.destroyAllWindows()
