# 🔧 용접 AI 학습 데이터셋 활용 프로젝트

본 프로젝트는 AIHub에서 제공하는 **창원 지역 특화산업 고도화 및 디지털 전환 촉진을 위한 용접 AI 학습 데이터셋**을 기반으로,  
용접 품질 판별, 이상 탐지 및 공정 자동화를 위한 인공지능 모델을 개발하는 데 목적이 있습니다.

📂 데이터 출처: [AIHub - 용접 AI 학습 데이터](https://www.aihub.or.kr/aihubdata/data/view.do?dataSetSn=71761)

---

## 📌 모델 정보

- **모델 명칭**: Yolov5x-seg
- **모델 버전**: 최신 커스텀 학습 버전
- **모델 Task**:
  - VT (Visual Testing, 육안검사)
  - RT (Radiographic Testing, 방사선 투과 검사)
- **모델 선정 이유**:  
  Yolov5는 다양한 크기와 형태의 객체를 정확하게 탐지하고 분류할 수 있는 강력한 성능을 보이는 모델로,  
  용접 결함처럼 다양한 크기와 형태를 갖는 객체를 처리하는 데 매우 적합합니다.  
  특히 Yolov5x-seg는 세분화(Segmentation)까지 가능해 결함 부위를 더욱 정밀하게 인식할 수 있습니다.  
  또한 경량화와 빠른 추론 속도 덕분에 실제 제조현장에서의 실시간 품질 판독에도 효과적입니다.

> ⚠️ **주의**: 학습된 모델 가중치 파일 `best.pt`는 GitHub 용량 제한으로 인해 저장소에 포함되어 있지 않습니다.  
> 해당 파일은 [AIHub](https://www.aihub.or.kr/aihubdata/data/view.do?dataSetSn=71761)에서 다운로드 받아 사용자의 환경에 수동으로 배치해야 합니다.

---

## 📦 데이터셋 개요

- **제공 기관**: AIHub (한국지능정보사회진흥원)
- **수집 대상**: 창원지역 제조 현장의 용접 공정 데이터
- **데이터 유형**:
  - 용접 영상 및 이미지 (RGB / 열화상 등)
  - 센서 기반 시계열 데이터
  - 품질 검사 결과 라벨
  - 음향/진동 데이터 등

---

## 📘 AI 모델 사용 메뉴얼

### 🔍 육안검사(VT)

- 사용 문서: `AI 모델 사용 메뉴얼_VT.hwp`
- 주요 내용:
  - 검사 이미지 입력 및 예측 실행 방법
  - 예측 결과 확인 방법
  - 결함 위치 시각화 및 판독 기준
  - 저장 및 리포트 기능 설명

### 💡 방사선 투과 검사(RT)

- 사용 문서: `AI 모델 사용 메뉴얼_RT.hwp`
- 주요 내용:
  - RT 촬영 이미지 기반 예측 수행 방식
  - 결함 탐지 알고리즘 구성
  - 모델 설정 값 및 커스텀 적용법
  - 결과 출력 구조 및 저장 방식

---

## 🚀 프로젝트 실행 방법

1. 저장소 클론:
   ```bash
   git clone https://github.com/yunseok451/weld_defects.git
   cd weld_defects
   ```

2. 의존성 설치:
   ```bash
   pip install -r requirements.txt
   ```

3. 모델 가중치 다운로드:
   - `best.pt` 파일은 [AIHub 데이터셋 링크](https://www.aihub.or.kr/aihubdata/data/view.do?dataSetSn=71761)를 통해 수동으로 다운로드하세요.
   - `docker_RT/` 또는 `docker_VT/` 내부의 해당 경로에 배치해야 합니다.

4. 학습 또는 추론 실행:
   ```bash
   python train.py  # or predict.py
   ```

---

## 🧰 기술 스택

- Python 3.8+
- PyTorch
- Ultralytics YOLOv5
- OpenCV
- Scikit-learn
- Pandas, NumPy

---

## 📜 라이선스 및 저작권

- 해당 데이터는 **AIHub 이용 정책**에 따라 사용 가능하며, 상업적 목적 사용 시 별도 승인이 필요할 수 있습니다.
- 본 프로젝트 코드는 MIT License 또는 별도 지정된 라이선스를 따릅니다.

---

## 🙋‍♂️ 문의

- 프로젝트 담당자: [@yunseok451](https://github.com/yunseok451)
- 데이터 관련 문의: [AIHub 공식 웹사이트](https://www.aihub.or.kr)
