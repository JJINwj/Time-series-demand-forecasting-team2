비트코인 주가 예측 프로젝트: Raw Data

비트코인 주가 예측 프로젝트에서 Binance 거래소의 BTCUSDT 1시간봉(1h) 시계열 데이터가 Raw Data로 사용된다.

1. BTCUSDT란?
  BTCUSDT는 가축 자산(BTC)과 호가 통화(USDT)으로 구성된 거래쌍(trading pair)이다.
  여기에서 BTC는 비트코인, USDT는 테더를 의미하고, 테더는 달러와 1:1로 연동된 스테이블코인을 말한다.

2. 데이터 기간
  BTCUSDT 거래쌍은 2017년 8월 17일에 Binance에서 처음 생성되었으므로, 데이터 기간은 2017-08-17 ~ 2025-11-26(현재)이다.

3. 데이터 간격
  일봉 데이터는 약 3,000개 수준으로 딥러닝 학습에는 부족하고, 분봉 데이터는 노이즈가 과도하다.
  따라서, 약 6만 개 이상의 충분한 시계열을 확보하면서도 변동성 패턴을 잘 반영하기 위해 1시간 간격 데이터를 사용한다.

4. 데이터 구성
  데이터를 구성하는 각 열과 그에 대한 설명은 다음과 같다.
  timestamp           : candle의 시작 시각 (Unix time, ms)
  open                : 시가 (해당 시간의 첫 거래 가격)
  high                : 고가 (해당 시간 중 가장 높은 가격)
  low                 : 저가 (해당 시간 중 가장 낮은 가격)
  close               : 종가 (해당 시간의 마지막 거래 가격, 예측 타깃)
  volume              : 해당 시간 동안 거래된 BTC 수량
  close_time          : candle의 종료 시각 (Unix time, ms)
  quote_asset_volume  : USDT 기준 거래량 (거래 금액 총합)
  num_trades          : 해당 시간 동안 체결된 거래 횟수
  taker_buy_base      : taker 매수 BTC 수량
  taker_buy_quote     : taker 매수 USDT 금액
  ignore              : 내부용 placeholder 필드 (사용되지 않음)
  
  * Unix time 
    : 컴퓨터 시스템에서 날짜·시간을 숫자로 표현하는 방식으로, 1970년 1월 1일 00:00:00 UTC부터 흐른 시간을 ‘초’ 또는 ‘밀리초(ms)’ 단위로 나타낸 값이다.
  * candle
    : 주식·암호화폐에서 많이 쓰는 가격 표시 방식으로, 일정 기간 동안의 시가(Open), 고가(High), 저가(Low), 종가(Close)를 하나의 블록로 묶어 표현한 것이다.
  * taker
    : 거래소에서 주문이 성립될 때, 이미 존재하는 호가를 가져가는 주문을 낸 사람을 말한다.
  * placeholder
    : 컴퓨터나 데이터 구조에서 자리를 채우기 위해 넣어둔 임시 값을 의미한다.
    
5. 데이터 수집 코드 (Binanace API 사용)
  아래는 BTCUSDT 1시간봉 전체 데이터를 자동으로 다운로드하는 Python 코드이다.
  API의 1000개 제한을 우회하기 위해, startTime을 주기적으로 업데이트하여 데이터를 여러 번 받고, 이어붙이는 방식이다.


# Download_RawData.py

import requests
import pandas as pd
import time

# Binance Kline 데이터 요청 함수
def get_binance_klines(symbol="BTCUSDT", interval="1h", start_time=None, end_time=None, limit=1000):
    url = "https://api.binance.com/api/v3/klines"
    params = {
        "symbol": symbol,
        "interval": interval,
        "startTime": start_time,
        "endTime": end_time,
        "limit": limit
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

# BTCUSDT 1시간봉 전체 다운로드 함수
def download_btcusdt_hourly(start_date="2017-08-17"):
    start_ms = int(pd.Timestamp(start_date).timestamp() * 1000)
    end_ms = int(pd.Timestamp.now().timestamp() * 1000)

    all_rows = []
    current = start_ms

    print("📥 BTCUSDT 1시간봉 다운로드 시작...")

    # API 제한을 피하기 위한 반복 호출
    while current < end_ms:
        data = get_binance_klines(
            symbol="BTCUSDT",
            interval="1h",
            start_time=current
        )

        if len(data) == 0:
            break

        all_rows.extend(data)

        # 다음 요청을 위해 마지막 캔들의 close_time 이후로 이동
        current = data[-1][6] + 1

        time.sleep(0.4)  # API rate-limit 보호용

        print("✔ 진행:", pd.to_datetime(current, unit='ms'))

    print("📦 다운로드 완료. DataFrame으로 변환 중...")

    columns = [
        "timestamp", "open", "high", "low", "close", "volume",
        "close_time", "quote_asset_volume", "num_trades",
        "taker_buy_base", "taker_buy_quote", "ignore"
    ]

    df = pd.DataFrame(all_rows, columns=columns)

    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")

    df.to_csv("BTCUSDT_1h_raw.csv", index=False)
    print("💾 저장 완료: BTCUSDT_1h_raw.csv")

if __name__ == "__main__":
    download_btcusdt_hourly()
