import os
import fiftyone as fo
from fiftyone import ViewField as F

# 이미지 데이터와 애너테이션을 포함하는 디렉토리 경로로 설정합니다.
base_dir = "/Users/neo/fiftyone/coco-2017"  # 이 경로를 실제 COCO 데이터셋 폴더 경로로 변경하세요.

dataset_dirs = {
    "train": {
        "data": os.path.join(base_dir, "train"),
        "labels": os.path.join(base_dir, "train/labels.json"),
    },
    "validation": {
        "data": os.path.join(base_dir, "validation"),
        "labels": os.path.join(base_dir, "validation/labels.json"),
    },
    "test": {
        "data": os.path.join(base_dir, "test"),
        "labels": os.path.join(base_dir, "test/labels.json"),
    },
}
# Train 데이터셋 로드
train_dataset = fo.Dataset.from_dir(
    dataset_dirs["train"]["data"],
    dataset_type=fo.types.COCODetectionDataset,
    labels_path=dataset_dirs["train"]["labels"],
)
train_dataset.add_sample_field(
    "ground_truth_detections", fo.EmbeddedDocumentField, ftype=fo.fields.DetectionsField
)

# validation 데이터셋 로드
val_dataset = fo.Dataset.from_dir(
    dataset_dirs["validation"]["data"],
    dataset_type=fo.types.COCODetectionDataset,
    label_field="ground_truth_detections",
    labels_path=dataset_dirs["validation"]["labels"],
)

# # Test 데이터셋 로드
# test_dataset = fo.Dataset.from_dir(
#     dataset_dirs["test"]["data"],
#     dataset_type=fo.types.ImageDirectory,
#     label_field="ground_truth_detections",
#     labels_path=dataset_dirs["test"]["labels"],
# )
# ================ # 로드 

# 경계선 이후 추가된 코드 수정
label_field = "ground_truth_detections" 
view1 = train_dataset.select_fields(label_field)
view2 = val_dataset.select_fields(label_field)

# Export the YOLOv5-compatible dataset
export_dir = "/Users/neo/fiftyone/yolo"
splits = ["train", "validation"]
classes = ["bicycle", "motorcycle", "bus", "truck", "car"]

for split in splits:
    split_view = view1.match(F("tags").contains(split))
    split_view.export(
        export_dir=export_dir,
        dataset_type=fo.types.YOLOv5Dataset,
        label_field=label_field,
        split=split,
        classes=classes,
    )
for split in splits:
    split_view = view2.match(F("tags").contains(split))
    split_view.export(
        export_dir=export_dir,
        dataset_type=fo.types.YOLOv5Dataset,
        label_field=label_field,
        split=split,
        classes=classes,
    )
