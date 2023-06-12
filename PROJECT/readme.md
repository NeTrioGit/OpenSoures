## 퀵보드 후방 주시 위험 알림
퀵보드 후방 주시 위험 알림 프로젝트는 COCO-2017의 ['bicycle', 'motorcycle', 'bus', 'truck', 'car']에 해당하는 데이터셋과 https://universe.roboflow.com/chexml/scooter_images 에서 ['scooter']에 해당하는 데이터셋을 YOLOv8 https://github.com/ultralytics/ultralytics 으로 모델을 학습시켜 구현하였습니다.

## 1. 가상환경 구현 (mac m1 환경)

### 1.1. Homebrew 설치
먼저, Mac용 [Homebrew](https://brew.sh/) 패키지 관리자를 설치합니다.

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
### 1.2. Miniforge 설치
Homebrew를 이용해 miniforge를 설치합니다.

```bash
brew install miniforge
```
### 1.3. YOLOv8 가상환경 생성
Miniforge로 YOLOv8이라는 이름의 가상환경을 만듭니다.

```bash
conda create -n YOLOv8 python=3.9
```
### 1.4. 가상환경 활성화
가상환경을 활성화합니다.

```bash
conda activate YOLOv8
```

## 2. 커스텀 데이터셋 만들기

### 2.1. COCO-2017 데이터셋 다운로드

1. 가상환경에 fiftyone 라이브러리를 설치합니다.

```bash
pip install fiftyone
```

2. COCO-2017 데이터셋을 다운로드합니다.

다운 실행.py 실행파일 참고

3. coco(json)형식 -> yolo형식 변환합니다.

 (1) coco-2017(yolo).py - 정상 실행
 (2) json-yolo형식 변환.py - 오류 발생

### 2.2. 스쿠터 이미지 데이터셋 다운로드

https://universe.roboflow.com/chexml/scooter_images
위 주소에서 스쿠터 이미지 데이터셋을 YOLOv8 형식으로 다운로드합니다.

다운로드한 파일을 원하는 디렉터리에 위치시킵니다.

### 2.3. 두 데이터셋 병합하기

1. 두 데이터셋을 디렉토리에 함치기에 앞서 json-yolo형식 변환.py 코드를 이용해서 

coco데이터셋에서 ['bicycle', 'motorcycle', 'bus', 'truck', 'car']를 0~4번으로 수정

스쿠터데이터셋에서  ['scooter'] 라벨을 제외한 다른 라벨을 제거 후 5번으로 수정
 * 라벨을 수정한 이후 라벨 값이 존재하지 않는 빈 데이터셋은 반드시 따로 제거 해야한다.

2. 다운 받은 두 데이터셋을 각각의 train 디렉토리와 val 디렉토리로 옮긴다.

3. data.yaml 작성한다.

```yaml
train: /Users/neo/Downloads/dataset/train/images
val: /Users/neo/Downloads/dataset/valid/images

nc: 6
names: ['bicycle', 'motorcycle', 'bus', 'truck', 'car', 'scooter']
```

## 3. 커스텀 데이터 학습하기

### 3.1. YOLOv8 설치
Ultralytics 라이브러리 설치
학습 과정에서 필요한 YOLOv8 알고리즘을 사용하기 위해 Ultralytics를 설치한다.

```bash
pip install ultralytics
```

### 3.2. 학습 코드 작성 및 실행

모델학습(v8nano).py 실행파일 참고
사전 훈련 된 가중치인 "yolov8n.pt"를 사용하여 YOLO 객체를 생성 & 초기화

 epochs = 전체 훈련 세트를 알고리즘에 거쳐 학습 시키는 전체 횟수
 imgsz = 입력 이미지의 크기를 정의

 이전에 훈련 중이던 모델에 이어서 훈련 시키는 방법
 모델학습(last).py 실행파일 참고
 
### 3.3. 학습된 모델로 예측 수행하기

Ultralytics YOLOv8 Docs 에서 제공하는 코드로 실행
 https://docs.ultralytics.com/modes/track/

 모델 실행(추적).py
 모델 실행(추적,cv2).py 실행파일 참고

 ### 3.4. 학습된 모델을 다른 형식으로 내보내기

 내보내기.py 실행파일 참고