import fiftyone as fo
from fiftyone import ViewField as F

dir_path = "/Users/neo/fiftyone/coco-2017"  # Modify this directory path

dataset = fo.Dataset.from_dir(
    dir_path,
    dataset_type=fo.types.FiftyOneDataset,  # Specify dataset type
)

# Create a view with the desired label field
label_field = "ground_truth"  # Modify this if necessary
view = dataset.select_fields(label_field)

# Export the YOLOv5-compatible dataset
export_dir = "/Users/neo/fiftyone/yolo"
label_field = "ground_truth"
splits = ["train", "validation"]
classes = ["bicycle", "motorcycle", "bus", "truck", "car"]

for split in splits:
    split_view = view.match(F("tags").contains(split))
    split_view.export(
        export_dir=export_dir,
        dataset_type=fo.types.YOLOv5Dataset,
        label_field=label_field,
        split=split,
        classes=classes,
    )
