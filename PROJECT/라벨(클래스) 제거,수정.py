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
###########
data_coco_train = foz.load_zoo_dataset("coco-2017", split="train", classes=target_classes)

import fiftyone as fo
import fiftyone.zoo as foz

target_classes = ["bicycle", "motorcycle", "bus", "truck", "car"]

# Load COCO train dataset with the target classes
data_coco_train = foz.load_zoo_dataset("coco-2017", split="train", classes=target_classes)

# Launch the FiftyOne App to visualize the filtered dataset
session = fo.launch_app(data_coco_train)

session.wait()

#######
# #
# #--
# --
# --------_#############

import fiftyone as fo
import fiftyone.zoo as foz

target_classes = ["bicycle", "motorcycle", "bus", "truck", "car"]

# Load COCO train dataset
data_coco_train = foz.load_zoo_dataset("coco-2017", split="train", download=False)

def filter_detections(sample):
    filtered_detections = []
    for detection in sample.ground_truth.detections:
        if detection.label in target_classes:
            filtered_detections.append(detection)
    sample.ground_truth.detections = filtered_detections
    sample.save()

# Apply the filtering function to the dataset
data_coco_train.foreach(filter_detections)

# Launch the FiftyOne App to visualize the filtered dataset
session = fo.launch_app(data_coco_train)

session.wait()
