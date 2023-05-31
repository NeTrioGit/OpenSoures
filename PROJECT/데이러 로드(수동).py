import fiftyone as fo
from fiftyone import ViewField as F

# Define the paths to the JSON annotations and image directory
annotations_path = "/Users/neo/fiftyone/coco-2017/new/train/labels.json"
image_dir = "/Users/neo/fiftyone/coco-2017/train/data"

# Create a FiftyOne dataset from the JSON annotations and image directory
dataset = fo.Dataset.from_dir(
    dataset_type=fo.types.COCODetectionDataset,
    data_path=image_dir,
    labels_path=annotations_path,
)

# Launch the FiftyOne App to visualize the dataset
session = fo.launch_app(dataset)

# Wait for the app to close
session.wait()