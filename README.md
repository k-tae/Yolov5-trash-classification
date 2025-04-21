# YOLOv5를 이용한 쓰레기 분류

본 프로젝트는 **YOLOv5 객체 탐지 기술**을 활용하여 다양한 쓰레기를 자동으로 인식하고 분류하는 시스템을 구현한 연구입니다. 재활용을 촉진하고 환경 오염을 줄이기 위한 목적으로 개발되었습니다.

## 🧠 프로젝트 개요

- **목적**: 쓰레기 자동 분류를 통해 재활용 효율 향상 및 환경 보호
- **기술**: YOLOv5 (PyTorch 기반 실시간 객체 탐지 모델)
- **데이터셋**: AIHub 생활 폐기물 이미지 데이터 (총 15종 중 5종 사용)
- **분류 대상**: 비닐류, 유리병류, 종이류, 캔류, 페트병류

## 📁 데이터 처리

- AIHub에서 제공한 JSON 라벨링 데이터를 YOLOv5 형식의 `.txt` 파일로 전처리
- 이미지 당 `class x_center y_center width height` 형식 사용

## ⚙️ 모델 학습

- **플랫폼**: Google Colab (GPU 사용)
- **하이퍼파라미터**:
  - `batch size`: 8
  - `epochs`: 25 (과적합 방지 목적)
- **성능 평가**: Precision, Recall 등을 통해 평가

## 📊 학습 결과

YOLOv5 모델은 `runs/train/trash_results3` 디렉토리에서 다음과 같은 학습 성과 지표를 생성했습니다.

| Loss & mAP | Confusion Matrix | PR Curve |
|:----------:|:----------------:|:--------:|
| ![](runs/train/trash_results3/results.png) | ![](runs/train/trash_results3/confusion_matrix.png) | ![](runs/train/trash_results3/PR_curve.png) |


## ✅ 결과 요약

- **정확한 분류**: 비닐류, 캔류, 유리병류
- **부정확한 분류**: 종이류, 페트병류 (형태 변화에 취약)
- **한계**: 객체가 여러 개인 경우 하나로 인식하는 오류

### 📸 분류 예시 결과

#### 🥫 캔류 예측
<p float="left">
  <img src="runs/detect/can.jpg" width="250"/>
  <img src="runs/detect/can2.jpg" width="250"/>
</p>

#### 🍾 유리병류 예측
<p float="left">
  <img src="runs/detect/glass.jpg" width="250"/>
  <img src="runs/detect/glass2.jpg" width="250"/>
</p>

#### 🛍️ 비닐류 예측
<p float="left">
  <img src="runs/detect/vinyl.jpg" width="250"/>
  <img src="runs/detect/vinyl2.jpg" width="250"/>
</p>

#### 📄 종이류 예측
<p float="left">
  <img src="runs/detect/milk.png" width="250"/>
</p>

#### 🧴 페트병류 예측
<p float="left">
  <img src="runs/detect/plastic.jpg" width="250"/>
</p>

## 🔧 향후 개선 방향

- 다양한 형태의 쓰레기 이미지 추가 (구겨진 종이, 찌그러진 병 등)
- 다객체 인식이 가능한 구조로 모델 개선
- 전체 클래스(15종) 학습으로 확대

## 🗝️ 주요 키워드

`YOLOv5` `Object Detection` `Garbage Classification` `Recycling` `Computer Vision`
