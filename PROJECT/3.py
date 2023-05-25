#라벨제거

import fiftyone as fo
from fiftyone import ViewField as F

# 데이터셋 로드
dataset = fo.load_dataset("coco-2017")

# 수정할 클래스 지정
target_classes = ["bicycle", "motorcycle", "bus", "truck", "car"]

# target_classes에 해당하지 않는 라벨을 제거하는 필터 생성
filter_expr = F("ground_truth.detections.label").is_in(target_classes)

# 필터를 적용하여 라벨 일괄 수정
dataset = dataset.filter_labels("ground_truth", filter_expr)

# 수정된 데이터셋을 저장
dataset.save()

###########################
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


