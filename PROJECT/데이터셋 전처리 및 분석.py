import fiftyone as fo
import fiftyone.zoo as foz

target_classes = ["bicycle", "motorcycle", "bus", "truck", "car"]

# Load COCO2017 train dataset, downloading if necessary
train_dataset = foz.load_zoo_dataset("coco-2017", split="train", classes=target_classes)

# Apply MongoDB data aggregation to get the label distribution
label_distributions = train_dataset.count_sample_tags()

print(label_distributions)

# Split the dataset into train, validation and test datasets
train_dataset, val_dataset, test_dataset = fo.load_zoo_dataset(
    "coco-2017",
    split="train",
    classes=target_classes
).split_sample([0.8, 0.1, 0.1])
