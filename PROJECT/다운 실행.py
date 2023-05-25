import fiftyone as fo
import fiftyone.zoo as foz

# 원하는 클래스 지정: bicycle, motorcycle, bus, truck, car
target_classes = ["bicycle", "motorcycle", "bus", "truck", "car"]

# 데이터셋 다운로드
dataset = foz.load_zoo_dataset(
    "coco-2017",
    split="train",
    classes=target_classes
)

# GUI에서 시각화
session = fo.launch_app(dataset)

session.wait()