import fiftyone as fo
import fiftyone.zoo as foz

target_classes = ["bicycle", "motorcycle", "bus", "truck", "car"]

# Load COCO train dataset (coco-2017에 맞게 수정 필요)
data_coco_train = foz.load_zoo_dataset("coco-2017", split="train", classes=target_classes)

def filter_detections(sample):
    filtered_detections = []
    for detection in sample.ground_truth.detections:
        if detection.label in target_classes:
            filtered_detections.append(detection)
    return fo.Detections(detections=filtered_detections)

data_coco_train.map_labels("ground_truth", filter_detections)

# GUI에서 시각화
session = fo.launch_app(data_coco_train)

session.wait()