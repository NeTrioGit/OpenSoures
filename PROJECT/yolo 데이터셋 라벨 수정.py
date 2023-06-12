import os

# /Users/neo/Downloads/dataset/test/labels
# /Users/neo/Downloads/dataset/train/labels
# /Users/neo/Downloads/dataset/vaild/labels
input_dir = '/Users/neo/Downloads/dataset/valid/labels'
label_mapping = {0: 5}  # 원하는 숫자 라벨에 대한 매핑. 예: 기존 라벨 1을 2로 변경하고, 3을 4로 변경
labels_to_delete = {4}  # 삭제할 숫자 라벨 설정

for file in os.listdir(input_dir):
    if file.endswith('.txt'):
        file_path = os.path.join(input_dir, file)

        with open(file_path, 'r') as file:
            lines = file.readlines()

        with open(file_path, 'w') as file:
            for line in lines:
                line_parts = line.strip().split(' ')
                label_index = int(line_parts[0])

                # 라벨 명칭 변경
                if label_index in label_mapping:
                    label_index = label_mapping[label_index]

                # 특정 라벨 명칭 삭제
                if label_index not in labels_to_delete:
                    line_parts[0] = str(label_index)
                    file.write(' '.join(line_parts) + '\n')
