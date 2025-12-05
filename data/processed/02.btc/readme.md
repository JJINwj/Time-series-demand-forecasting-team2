# 비트코인 주가 예측 프로젝트: Processed Data

비트코인 주가 예측 프로젝트에서는 머신러닝 사용을 위해 피처 엔지니어링 (Feature engineering)을 실시한다. 선정된 피처들은 논문에 근거한다.

---
**1. 가격 기반 (Price-based) Features**
  * 로그 수익률 (Log Return)
  * 여기에서 BTC는 비트코인, USDT는 테더를 의미하고, 테더는 달러와 1:1로 연동된 스테이블코인을 말한다.
log_returnt​=ln(Closet−1​Closet​​)
---
**2. 데이터 기간**
  * CryptoDataDownload에서 제공하는 BTCUSDT 거래쌍 데이터는 2017-8-17 04:00:00 부터 2025-12-02 23:00:00 까지 존재한다.
    
    (25년 12월 4일 기준)

---
**3. 데이터 간격**
  * 일봉 데이터는 약 3,000개 수준으로 딥러닝 학습에는 부족하며, 분봉 데이터는 과도한 노이즈가 포함된다.
  * 따라서, 약 6만 개 이상의 충분한 데이터을 확보하면서도 변동성 패턴을 잘 반영하기 위해 시간봉 데이터를 사용한다.

---
**4. 데이터 구성 (btc_processed.csv)**
  * 데이터를 구성하는 각 열과 그에 대한 설명은 다음과 같다.
  * log_return          : 직전 시간 대비 로그 수익률
  * abs_return          : 로그 수익률의 절대값 (변동성 크기 반영)
  * return_5            : 지난 5시간 동안의 종가 변화율
  * return_24           : 지난 24시간 동안의 종가 변화율
  * high_low_range      : 시가 대비 고저차 비율 (단기 변동성 지표)
  * Close_open          : 시가 대비 종가의 비율 변화
  * upper_shadow        : 고가 - max(시가,종가)
  * lower_shadow        : min(시가,종가) - 저가
  * real_body           : candle 크기
  * tradecount          : 해당 시간 동안 체결된 거래 횟수

  * volume_z	          : 지난 24시간 거래량의 표준화 Z-score
  * volume_change	      : 거래량 변화율

  * buy_ratio	          : 매수 비율(taker_buy_base / volume_btc)
  * buy_quote_ratio	    : 매수 비율(USDT 기준 거래량 대비)
  * order_imbalance     :	매수량 − 매도량으로 계산한 거래 불균형

  * rolling_vol_24      :	최근 24시간 로그수익률 표준편차(단기 변동성)
  * rolling_vol_168     :	최근 168시간(1주) 로그수익률 변동성
  * parkinson_vol       :	고가–저가 구간을 이용한 변동성 추정치

  * SMA_5               :	5시간 단순 이동평균
  * SMA_10              :	10시간 단순 이동평균
  * SMA_20              :	20시간 단순 이동평균
  * EMA_12              :	12시간 지수 이동평균
  * EMA_26              :	26시간 지수 이동평균
  * MACD	              : EMA12 − EMA26 (대표 추세·모멘텀 지표)
  * RSI	                : 14시간 RSI (가격 상승·하락 강도 지표)

  * skew_24	            : 최근 24시간 수익률 분포의 비대칭도
  * kurt_24	            : 최근 24시간 수익률 분포의 첨도(꼬리 두께)

  * TR	                : True Range(가격 변동폭: 고가·저가·전 종가 기반)
  * ATR_14	            : 14시간 평균 True Range(변동성 강도 지표)

  * hour                :	해당 시각의 시간(0~23)
  * dayofweek	          : 요일(월=0, 일=6) — 시간대별/요일별 패턴 반영

  * return_mean_24	    : 최근 24시간 로그수익률 평균
  * return_std_24       :	최근 24시간 로그수익률 표준편차
  * body_mean_24        :	최근 24시간 가격 몸통 크기 평균
  
  > Unix time 
    : 컴퓨터 시스템에서 날짜·시간을 숫자로 표현하는 방식으로, 1970년 1월 1일 00:00:00 UTC부터 흐른 시간을 ‘초’ 또는 ‘밀리초’ 단위로 나타낸 값이다.

  > candle 
    : 주식·암호화폐에서 많이 쓰는 가격 표시 방식으로, 일정 기간 동안의 시가(Open), 고가(High), 저가(Low), 종가(Close)를 하나의 블록로 묶어 표현한 것이다.

---
**5. 데이터 수집 방식**
  * CryptoDataDownload에서 제공하는 CSV 파일을 그대로 Raw Data로 사용한다.
  * 링크는 다음과 같다: https://www.cryptodatadownload.com/data/binance/#google_vignette


**6. 참고문헌**
  * Cont, R. (2001). Empirical properties of asset returns: Stylized facts and statistical issues. Quantitative Finance, 1(2), 223–236.
  * Parkinson, M. (1980). The extreme value method for estimating the variance of the rate of return. Journal of Business, 53(1), 61–65.
  * Karpoff, J. M. (1987). The relation between price changes and trading volume: A survey. Journal of Financial and Quantitative Analysis, 22(1), 109–126.
  * Easley, D., López de Prado, M., & O’Hara, M. (2012). The microstructure of the stock market. Journal of Portfolio Management.
  * Andersen, T. G., & Bollerslev, T. (1998). Answering the skeptics: Yes, standard volatility models do provide accurate forecasts. International Economic Review, 39(4), 885–905.
  * Jegadeesh, N., & Titman, S. (1993). Returns to buying winners and selling losers: Implications for stock market efficiency. Journal of Finance, 48(1), 65–91.
  * Kim, J. H., & White, H. (2004). Consistent VK testing for structural breaks in GARCH models. Journal of Econometrics, 122(1), 225–250.
  * Caporale, G. M., & Plastun, A. (2018). Calendar anomalies in the cryptocurrency market. Finance Research Letters.


