# Time-series-demand-forecasting-team2
시계열 기반 수요 예측 프로젝트 (2팀 프로젝트 작업 공간) 
## 1. 팀 정보 (수정예정)

- 팀 번호: 1팀

- 팀명: Urban Infrastructure Prediction

- 팀원:

  - 김경식 (PM, 전기차 충전량 데이터·모델링)

  - 김우석 (교통량 데이터·시계열 모델링·발표)


## 2. 프로젝트 개요 (수정예정)

- 한 줄 설명:

  - 예) 서울시 전기차 충전량과 방향별 회전 교통량 데이터를 분석·예측하여, 도시 인프라 수요 패턴과 피크 시간대를 파악하는 프로젝트입니다.

- 키워드:

  - #서울시 #전기차충전 #교통량 #시계열 #수요예측


## 3. 데이터 소개 (수정예정)

- 출처:

  - 서울열린데이터광장: (데이터셋 이름/링크)

  - 기타: TAAS, 경찰청 사고 통계 등 (해당되는 경우만)

- 주요 컬럼:

  - 예) `gu_name`, `station_id`, `charge_type`, `start_time`, `end_time`, `kwh`, ...

- 기간:

  - 예) 2023-01-01 ~ 2023-12-31

- 전처리 개요:

  - 결측치 처리, 이상치 제거, 시간 단위 리샘플링, 좌표 변환 등 간단 요약


## 4. 분석/모델링 목표 (수정예정)

- 분석 질문:

  1. 자치구/충전소 유형별 전력 사용량 패턴은 어떻게 다른가?

  2. 시간대별 충전량 피크는 언제 발생하는가?

- 사용 방법:

  - EDA: 시계열 플롯, 히트맵, 상자그림 등

  - 모델링: RandomForestRegressor, XGBoost 등 회귀 모델 비교

  - (선택) LLM: 결과 리포트 요약/설명문 생성


## 5. 폴더 구조 (수정예정)

```text

(project-root 구조 삽입)
project-root/
├── data/ #PM(따릉이+기상 merge 파일 interim 반영, 전처리 요청)
│   ├── raw/              # 원본 데이터(따릉이 원본, 기상원본, BTC 원본 등)
│   ├── interim/          # 1차 전처리 결과(중간 저장, merge 완료, 이상치 제거 완료 등)
│   └── processed/        # 최종 분석용 데이터(최종분석 및 모델링에 사용되는 최종 데이터 셋)
│
├── notebooks/ 
│   ├── 01_eda.ipynb      # 데이터 탐색(EDA), 히스토그램, 박스플롯, 기초통계 
│   ├── 02_feature_engineering.ipynb # 파생변수 생성, 날짜변수/lag/rolling 생성
│   ├── 03_modeling_timeseries.ipynb # 선형회귀, 랜덤포레스트, XG Boost/ ARIMA/LSTM 모델링
│   └── 04_visualization_report.ipynb # 최종결과 그래프 생성 및 인사이트 정리(보고서용)
│
├── src/ #공통함수모음, 라이브러리 역할
│   ├── data_loader.py #CSV/Excel 불러오는 함수 저장
│   ├── preprocessing.py #결측치 제거, 이상치 처리 등 전처리 함수
│   ├── features.py #날짜 파생변수(lag, rolling, month…) 생성 함수
│   ├── modeling_timeseries.py #모델링 함수(LinearRegression, RandomForest, XGBoost…)
│   └── visualization.py #그래프 그리는 함수 (heatmap, 예측 플롯 등)
│
├── reports/
│   ├── figures/ #시각화된 그래프 이미지들 저장(PNG/JPG)
│   └── final_report.md #최종 보고서(=README 복사본 or 추가 문서)
│
└── config/
    └── params.yaml
