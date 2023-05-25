import fiftyone.zoo as foz
# 수동 데이서텟 로드
# First parse the manually downloaded files in `source_dir`
foz.download_zoo_dataset(
    "bdd100k", source_dir="/path/to/dir-with-bdd100k-files"
)

# Now load into FiftyOne
dataset = foz.load_zoo_dataset("bdd100k", split="validation")

# 예시
# Import a random subset of 10 samples from the zoo dataset
dataset = foz.load_zoo_dataset(
    "cifar10",
    split="test",
    dataset_name="cifar10-test-sample",
    shuffle=True,
    max_samples=10,
)