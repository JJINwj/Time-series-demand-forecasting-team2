# 비트코인 주가 예측 프로젝트: Raw Data

비트코인 주가 예측 프로젝트에서는 CryptoDataDownload에서 제공하는 Binance 거래소의 BTCUSDT 1시간봉 시계열 데이터를 Raw Data로 사용한다.

---
**1. BTCUSDT란?**
  * BTCUSDT는 가축 자산(BTC)과 호가 통화(USDT)으로 구성된 거래쌍(trading pair)이다.
  * 여기에서 BTC는 비트코인, USDT는 테더를 의미하고, 테더는 달러와 1:1로 연동된 스테이블코인을 말한다.

---
**2. 데이터 기간**
  * CryptoDataDownload에서 제공하는 BTCUSDT 거래쌍 데이터는 2017-8-17 04:00:00 부터 2025-12-02 23:00:00 까지 존재한다.
    (25년 12월 4일 기준)

---
**3. 데이터 간격**
  * 일봉 데이터는 약 3,000개 수준으로 딥러닝 학습에는 부족하며, 분봉 데이터는 과도한 노이즈가 포함된다.
  * 따라서, 약 6만 개 이상의 충분한 데이터을 확보하면서도 변동성 패턴을 잘 반영하기 위해 시간봉 데이터를 사용한다.

---
**4. 데이터 구성 (Binance_BTCUSDT_1h.csv)**
  * 데이터를 구성하는 각 열과 그에 대한 설명은 다음과 같다.
  * Unix                : candle 시작 시각 (Unix time)
  * Date                : 날짜 및 시간 (UTC)
  * Symbol              : 거래쌍 이름 (BTCUSDT)
  * Open                : 시가 (해당 시간의 첫 거래 가격)
  * High                : 고가 (해당 시간 중 가장 높은 가격)
  * Low                 : 저가 (해당 시간 중 가장 낮은 가격)
  * Close               : 종가 (해당 시간의 마지막 거래 가격, 예측 타깃 변수)
  * Volume BTC          : 해당 시간 동안 거래된 BTC 수량
  * Volume USDT         : 해당 시간 동안 거래된 USDT 기준 거래량 (거래 금액 총합)
  * tradecount          : 해당 시간 동안 체결된 거래 횟수
  
  - Unix time 
    : 컴퓨터 시스템에서 날짜·시간을 숫자로 표현하는 방식으로, 1970년 1월 1일 00:00:00 UTC부터 흐른 시간을 ‘초’ 또는 ‘밀리초’ 단위로 나타낸 값이다.
  - candle
    : 주식·암호화폐에서 많이 쓰는 가격 표시 방식으로, 일정 기간 동안의 시가(Open), 고가(High), 저가(Low), 종가(Close)를 하나의 블록로 묶어 표현한 것이다.

---
**5. 데이터 수집 방식**
  * CryptoDataDownload (https://www.cryptodatadownload.com/data/binance/#google_vignette)에서 제공하는 CSV 파일을 그대로 Raw Data로 사용한다.



