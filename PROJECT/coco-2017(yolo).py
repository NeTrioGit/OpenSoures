import os
import shutil
import fiftyone as fo
import fiftyone.zoo as foz

def convert_to_yolo_format(sample, classes):
    label_str = ""
    if "ground_truth" in sample and sample["ground_truth"] is not None:
        for detection in sample["ground_truth"].detections:
            if detection.label not in classes:
                continue

            class_id = classes.index(detection.label)
            bbox = detection.bounding_box
            x_center, y_center, width, height = (
                bbox[0] + bbox[2] / 2,
                bbox[1] + bbox[3] / 2,
                bbox[2],
                bbox[3],
            )
            label_str += f"{class_id} {x_center} {y_center} {width} {height}\n"

    return label_str


def save_yolo_dataset(dataset, output_dir, classes):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for sample in dataset:
        label_str = convert_to_yolo_format(sample, classes)
        label_filepath = os.path.join(output_dir, os.path.splitext(sample.filepath.split("/")[-1])[0] + ".txt")

        with open(label_filepath, "w") as f:
            f.write(label_str)

        dst_image_path = os.path.join(output_dir, sample.filepath.split("/")[-1])
        shutil.copy(sample.filepath, dst_image_path)

    names_filepath = os.path.join(output_dir, "classes.names")
    with open(names_filepath, "w") as f:
        f.write("\n".join(classes))

splits = ["train", "validation", "test"]
classes = ["bicycle", "motorcycle", "bus", "truck", "car"]

for split in splits:
    print(f"처리 중: COCO 2017 {split} 데이터셋")
    coco_dataset = foz.load_zoo_dataset("coco-2017", split=split, dataset_name=f"coco-7{split}", classes=classes)

    output_dir = f"converted_yolo_coco_subset_{split}"
    save_yolo_dataset(coco_dataset, output_dir, classes)
