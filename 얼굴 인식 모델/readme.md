## 1.	얼굴 인식 원 소스 코드 주소 URL
 https://github.com/serengil/deepface

## 2.	자신이 찾은 얼굴인식 개요
라이브러리는 Python 언어로 됐으며, 딥러닝 모델을 이용하여 다양한 얼굴 인식 및 분석 을 하는 모델이다

이 deepface 라이브러리는 다양한 기능은 가지고 있다.
1) Face Verification: 두 개의 얼굴 이미지를 입력으로 받아, 두 얼굴이 동일한 사람인지 여부를 판단합니다.
2)	Face Recognition: 다수의 얼굴 이미지를 입력으로 받아, 각 얼굴 이미지가 어떤 사람의 것인지 인식합니다.
3)	Face Analysis: 입력된 얼굴 이미지에서 다양한 특징들을 추출하여 분석합니다. 예를 들어, 나이, 성별, 표정 등을 인식할 수 있습니다.
4)	Emotion Recognition: 입력된 얼굴 이미지에서 얼굴 표정을 인식하여, 해당하는 감정을 분류합니다.
5)	Facial Attribute Analysis: 입력된 얼굴 이미지에서 다양한 얼굴 속성을 분석합니다. 예를 들어, 안경 착용 여부, 수염 유무 등을 인식할 수 있습니다.
6)	Face Alignment: 얼굴 이미지에서 얼굴을 찾아 정렬합니다.
7)	Face Detection: 입력된 이미지에서 얼굴을 찾아냅니다.

그리고 이 라이브러리는 다양한 딥러닝 모델을 지원한다. 예를 들어 VGG-Face, Google FaceNet, OpenFace, 마지막으로 페이스북의 deepface 모델을 예로 들 수 있다.
## 3.	장단점 분석
장점:
간편한 사용성: DeepFace 라이브러리는 간단한 파이썬 API를 통해 사용할 수 있습니다. 이 라이브러리를 사용하면 얼굴 인식, 유사도 측정 등의 작업을 수행할 수 있습니다.

높은 정확성: DeepFace는 VGGFace2, FaceNet 등과 같은 최신 딥 러닝 모델을 사용합니다. 이러한 모델들은 고도로 정교하게 훈련되어 있으며, 얼굴 인식과 관련된 작업에서 높은 정확도를 제공합니다.

다양한 기능: DeepFace 라이브러리는 얼굴 인식, 유사도 측정, 감정 인식, 인종 인식 등 다양한 작업을 수행할 수 있습니다. 또한, 다양한 언어 (예: 파이썬, 자바스크립트 등)에서 사용할 수 있습니다.

오픈 소스: DeepFace 라이브러리는 오픈 소스로 제공됩니다. 이러한 이유로, 사용자들은 자유롭게 이 라이브러리를 수정하고 개선할 수 있습니다.

단점:

자원 소모: DeepFace 라이브러리는 많은 양의 메모리와 GPU를 필요로 합니다. 이러한 이유로, 높은 사양의 하드웨어가 필요할 수 있습니다.

데이터 양의 의존성: DeepFace는 대규모 데이터셋을 기반으로 학습됩니다. 이러한 이유로, 작은 데이터셋에서는 정확도가 낮을 수 있습니다.

언어 제한: DeepFace 라이브러리는 파이썬을 비롯한 몇 가지 언어에서만 사용할 수 있습니다. 이러한 이유로, 다른 언어를 사용하는 사용자들은 다른 라이브러리를 찾아야 할 수 있습니다.

## 4. 실행 결과

### Test1

####img1 과 img2

<img src="https://user-images.githubusercontent.com/112689981/233839372-5a2fbbde-0928-4947-ab4b-1a56dcc973f1.jpg" width="300" height="400"/><img src="https://user-images.githubusercontent.com/112689981/233839380-201070f6-add2-4714-967e-372b69762090.jpg" width="300" height="400"/>

<img width="192" alt="스크린샷 2023-04-23 오후 9 15 01" src="https://user-images.githubusercontent.com/112689981/233839391-fdbd6487-8f1b-47c0-8f93-306850a2903a.png">
####img1 과 img3

<img src="https://user-images.githubusercontent.com/112689981/233839425-35b2890a-6174-4f1b-a835-25ff9fbd7ebf.jpg" width="300" height="400"/><img src="https://user-images.githubusercontent.com/112689981/233839428-e285be80-4b61-4a5e-86dc-b4b7be624160.jpg" width="300" height="400"/>

<img width="200" alt="스크린샷 2023-04-23 오후 9 11 46" src="https://user-images.githubusercontent.com/112689981/233839431-4685d4df-4563-48b8-a1f1-5af6f3f75eb9.png">


## 5.어려웠던 점
 1) window환경이 아니라 mac m1환경에서 작업했기 때문에 Miniconda를 실치해서 파이썬 가상환경을 만들어야 했던 점에서 어려움이 있었다.
  추가로 miniconda를 활용하기 전에 ANACONDA3 와 Miniforge를 활용해서 파이썬 가상환경을 만들어 실행 하려 했지만 여전이 원인을 찾지 못했지만 지속전인 오류가 발생해서 3번째의 가상환경을 만들어서야 성공했다.
  
 2) 가상환경에서 tensorflow와 OpenCV, Deepface를 설치했음에도 바로 정상적으로 실행되지 않았고, 원인으로 openCV 공식 홈페이지에서 실행하는데 필요한 추가 파일을 다운받아 직접 특정 위치에 추가하는 과정을 가졌어야 했던 부분에서 어려움을 가졌다.

