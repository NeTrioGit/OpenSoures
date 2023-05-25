#FiftyOne 데이터셋을 YOLO 형식으로 변환
import os
import fiftyone as fo
import fiftyone.zoo as foz

# Load COCO2017 train dataset, downloading if necessary
train_dataset = foz.load_zoo_dataset("coco-2017", split="train", download=True)

# Specify output directories for YOLO-formatted dataset
output_dir = "/path/to/export/directory"
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
