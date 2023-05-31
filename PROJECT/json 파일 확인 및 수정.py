import json

def check_coco_json(json_path):
    with open(json_path, 'r') as f:
        coco_data = json.load(f)
    
    categories = set(category['id'] for category in coco_data['categories'])

    missing_categories = set()
    annotation_format_errors = []

    for annotation in coco_data['annotations']:
        category_id = annotation['category_id']

        if category_id not in categories:
            missing_categories.add(category_id)

        if 'image_id' not in annotation or 'bbox' not in annotation:
            annotation_format_errors.append(annotation)

    if len(missing_categories) > 0:
        print("Missing categories:", missing_categories)

    if len(annotation_format_errors) > 0:
        print("Annotations with format errors:", annotation_format_errors)

# 실행 코드
json_path = "/Users/neo/fiftyone/coco-2017/new/train/labels.json"

check_coco_json(json_path)

import json

json_file = '/Users/neo/fiftyone/coco-2017/new/train/labels.json'

with open(json_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

categories = data['categories']

# Check if Category ID 0 exists and add it if it doesn't
if not any(category['id'] == 0 for category in categories):
    new_category = {
        "id": 0,
        "name": "your_category_name_here_too"
    }
    categories.append(new_category)

# Save changes to the original JSON file
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Category ID 0 추가: {json_file}")
