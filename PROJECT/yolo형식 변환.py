#FiftyOne 데이터셋을 YOLO 형식으로 변환
import os
import fiftyone as fo
import fiftyone.zoo as foz

# Load COCO2017 train dataset, downloading if necessary
target_classes = ["bicycle", "motorcycle", "bus", "truck", "car"]

train_dataset = foz.load_zoo_dataset("coco-2017", split="train", classes=target_classes)

# Specify output directories for YOLO-formatted dataset
output_dir = "/Users/neo/fiftyone/yolo 형식 변환"
os.makedirs(output_dir, exist_ok=True)
os.makedirs(os.path.join(output_dir, "images", "train"), exist_ok=True)
os.makedirs(os.path.join(output_dir, "labels", "train"), exist_ok=True)

# Define function to convert FiftyOne dataset to YOLO format
def convert_and_export(dataset, output_dir, split="train"):
    for sample in dataset:
        labels = sample["ground_truth"].detections

        # Export image and labels to corresponding output directories
        sample.filepath = os.path.join(output_dir, "images", split, sample.filepath)
        sample.export_labels(labels, "yolo", os.path.join(output_dir, "labels", split))

# Convert train_dataset to YOLO format and save images and labels
convert_and_export(train_dataset, output_dir)

######
#######
##########
########
import os
import fiftyone as fo
import fiftyone.zoo as foz

# Load COCO2017 train dataset, downloading if necessary
target_classes = ["bicycle", "motorcycle", "bus", "truck", "car"]

train_dataset = foz.load_zoo_dataset("coco-2017", split="train", classes=target_classes)

# Specify output directories for YOLO-formatted dataset
output_dir = "/Users/neo/fiftyone/yolo 변환"
os.makedirs(output_dir, exist_ok=True)
os.makedirs(os.path.join(output_dir, "images", "train"), exist_ok=True)
os.makedirs(os.path.join(output_dir, "labels", "train"), exist_ok=True)

# Define function to convert FiftyOne dataset to YOLO format
def convert_and_export(dataset, output_dir, split="train"):
    for sample in dataset.iter_samples():
        # Export image
        sample.export(
            os.path.join(output_dir, "images", split),
            dataset_type="image",
            dataset_format="yolo",
        )

        # Export labels
        labels = sample["ground_truth"].detections
        label_content = ""

        for label in labels:
            class_name = label.label
            box = label.bounding_box
            x, y, width, height = box.left, box.top, box.width, box.height

            # Convert coordinates to YOLO format
            x_center = x + width / 2
            y_center = y + height / 2

            yolo_label = f"{class_name} {x_center} {y_center} {width} {height}\n"
            label_content += yolo_label

        with open(
            os.path.join(output_dir, "labels", split, f"{sample.id}.txt"), "w"
        ) as f:
            f.write(label_content)

# Convert train_dataset to YOLO format and save images and labels
convert_and_export(train_dataset, output_dir)
