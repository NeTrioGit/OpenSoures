import json
import os
from tqdm import tqdm

def coco_to_yolo(json_path, output_dir, images=None, categories=None):
    os.makedirs(output_dir, exist_ok=True)

    try:
        with open(json_path, 'r') as f:
            coco_data = json.load(f)
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error: {e}")
        return

    if images is None:
        images = {image['id']: image['file_name'] for image in coco_data['images']}
    if categories is None:
        categories = {category['id']: category['name'] for category in coco_data['categories']}

    # Rest of the original code
    # ...

    for annotation in tqdm(coco_data['annotations']):
        image_id = annotation['image_id']
        image_name = os.path.splitext(images[image_id])[0]
        category_id = annotation['category_id']

        try:
            category = categories[category_id]
        except KeyError:
            print(f"Warning: Category ID {category_id} not found in categories. Skipping this annotation.")
            continue

        bbox = annotation['bbox']
        x = bbox[0] + bbox[2] / 2
        y = bbox[1] + bbox[3] / 2
        width = bbox[2]
        height = bbox[3]

        file_path = os.path.join(output_dir, f"{image_name}.txt")

        with open(file_path, 'a') as file:
            file.write(f"{category} {x} {y} {width} {height}\n")

# 실행 코드
json_path = "/Users/neo/fiftyone/coco-2017/new/train/labels.json"
output_dir = "/Users/neo/YOLO_labels"

coco_to_yolo(json_path, output_dir)