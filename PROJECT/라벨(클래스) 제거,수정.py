import json
import os

with open("/Users/neo/fiftyone/coco-2017/train/labels.json") as f:
    data = json.load(f)

output_dir = "/Users/neo/fiftyone/coco-2017/new/train"
os.makedirs(output_dir, exist_ok=True)

target_classes = ["bicycle", "motorcycle", "bus", "truck", "car"]

# Filter categories
new_categories = [category for category in data["categories"] if category["name"] in target_classes]
category_id_map = {category["id"]: i for i, category in enumerate(new_categories)}

# Filter annotations
new_annotations = [ann for ann in data["annotations"] if ann["category_id"] in category_id_map]

# Update category_id in annotations
for ann in new_annotations:
    ann["category_id"] = category_id_map[ann["category_id"]]

# Update category_id in categories
for i, category in enumerate(new_categories):
    category["id"] = i + 1

# Filter images with filtered annotations
new_image_ids = list(set([ann["image_id"] for ann in new_annotations]))
new_images = [img for img in data["images"] if img["id"] in new_image_ids]

data["annotations"] = new_annotations
data["images"] = new_images
data["categories"] = new_categories

# Save new JSON file
with open(os.path.join(output_dir, "labels.json"), "w") as f:
    json.dump(data, f)