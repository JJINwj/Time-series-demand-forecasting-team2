# 비트코인 주가 예측 프로젝트: Processed Data

비트코인 주가 예측 프로젝트에서는 머신러닝 사용을 위해 피처 엔지니어링 (Feature engineering)을 실시한다. 각 피처들은 논문에 언급되었거나 또는 주가 예측에 일반적으로 사용되는 것으로 선정하였다.

---
**1. 가격 기반 피처 (Price-based Features)**
 * log_return

   : 직전 시간 대비 로그 수익률

   $log \\_ return_t = \ln{\left(\frac{Close_t}{Close_{t-1}}\right)}$

 * abs_return
 
   : 로그 수익률의 절대값 (변동성 크기 반영)

   $abs \\_ return_t = \left|log \\_ return_t\right|$
  
 * high_low_range
 
   :	시가 대비 고저차 비율 (변동성 지표)

   $high\\_low\\_range\_t = \frac{High\_t - Low\_t}{Open\_t}$ 
   
 * return_5
 
   :	지난 5시간 종가 변화율
  
   $return\\_5\_t = \frac{Close\_t - Close\_{t-5}}{Close\_{t-5}}$   
  
 * return_24

   : 지난 24시간 종가 변화율

   $return\\_24\_t = \frac{Close\_t - Close\_{t-24}}{Close\_{t-24}}$   
   
 * close_open
 
   : 시가 대비 종가 비율 변화

   $close\\_open_t = \dfrac{Close_t - Open_t}{Open_t}$
   
 * upper_shadow
 
   :고가 − max(시가, 종가)

   $upper\\_shadow\_t = High\_t - \max(Open\_t, Close\_t)$

 * lower_shadow

   : min(시가, 종가) − 저가

   $lower\_shadow\_t = \min(Open\_t, Close\_t) - Low\_t$
   
 * real_body	

   : 종가 − 시가의 절대값 (캔들 바디 크기)

   $real\\_body\_t = \left|Close\_t - Open\_t \right|$
  
---

**2. 거래량 기반 특징 (Volume-based Features)**
  * volume_z
    
   $volume\\_z\_t = \frac{Volume_t - \mu_{t-23t}}{\sig_{t-23t}}$
   
변화율 $volume\_change\_t = \frac{Volume\_t - Volume\_{t-1}}{Volume\_{t-1}}$
/ Volume Change: 거래량 급등락은 가격 방향성 변화의 대표적인 선행 지표로 알려져 있다.
  * 참고문헌: Karpoff, J. (1987). The relation between price changes and trading volume.
---
**3. 오더플로우 기반 특징 (Market Microstructure Features)**
  * 매수 비율(Buy Ratio), 매수–매도 불균형(Order Imbalance): 단기 수익률은 매수·매도 압력의 불균형에 의해 크게 좌우되며, 이는 시장 미시구조 분석에서 중요한 개념이다.
  * 수식: 매수 비율 $buy\_ratio\_t = \frac{taker\_buy\_base\_t}{volume\_btc\_t}$
         오더플로우 불균형 $order\_imbalance\_t = taker\_buy\_base\_t - (volume\_btc\_t - taker\_buy\_base\_t)$
  * 참고문헌: Easley, D., López de Prado, M., & O’Hara, M. (2012). The microstructure of the stock market.

4. 변동성 특징 (Volatility Features)
• Rolling Volatility (24h, 168h)

과거 변동성은 미래 변동성 예측에서 강력한 지표로 작용한다.

수식:
$rolling\_vol\_k(t) = std(log\_return\_{t-k+1:t})$

근거: Andersen, T., & Bollerslev, T. (1998). Volatility forecasting accuracy.

• Parkinson Volatility

고저차 기반 변동성 추정치는 전통적인 종가 기반 변동성보다 효율적이다.

수식:
$parkinson\_vol\_t = \sqrt{\frac{1}{4 \ln(2)} \left( \ln{\left(\frac{High\_t}{Low\_t}\right)} \right)^2 }$

5. 모멘텀 특징 (Momentum Indicators)
• SMA / EMA / MACD / RSI

추세 기반 모멘텀 지표는 과거 데이터의 자기상관 구조를 이용해 미래 수익률의 패턴을 포착할 수 있다.

수식:

SMA
$SMA\_k(t) = \frac{1}{k}\sum Close\_{t-i}$

EMA
$EMA\_t = \alpha Close\_t + (1-\alpha)EMA\_{t-1}$
$\alpha = 2/(k+1)$

MACD
$MACD\_t = EMA\_{12}(t) - EMA\_{26}(t)$

RSI
$RSI\_t = 100 - \frac{100}{1 + RS\_t}$

근거: Jegadeesh, N., & Titman, S. (1993). Returns to buying winners and selling losers.

6. 시장 구조 변화 특징 (Regime Change Indicators)
• Skewness / Kurtosis

수익률 분포의 비대칭성과 fat-tail 정도는 시장 상태(regime)의 변화를 반영하는 핵심 지표이다.

수식:

Skewness
$skew\_{24}(t) = \frac{E[(r-\mu)^3]}{\sigma^3}$

Kurtosis
$kurt\_{24}(t) = \frac{E[(r-\mu)^4]}{\sigma^4}$

근거: Kim, J., & White, H. (2004). Structural breaks in GARCH models.

7. 기술적 변동성 지표 (Technical Volatility Indicators)
• ATR (Average True Range)

가격 변동폭을 기반으로 변동성 강도와 추세 전환을 포착하는 대표적인 기술적 지표이다.

수식:

TR
$TR\_t = max(High\_t - Low\_t,\; |High\_t - Close\_{t-1}|,\; |Low\_t - Close\_{t-1}|)$

ATR
$ATR\_{14}(t) = \frac{1}{14}\sum TR\_{t-i}$

근거: Wilder, J. (1978). Technical Analysis.

8. 시간 기반 특징 (Time Features)
• Hour of Day / Day of Week

암호화폐 시장은 24시간 운영되며 시간대·요일별로 가격 변동성과 수익률 패턴이 달라지는 비효율성이 관측된다.

수식(개념적):

$hour = timestamp.hour$
$dayofweek = timestamp.dayofweek$

근거: Caporale, G., & Plastun, A. (2018). Calendar anomalies in the cryptocurrency market.
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
  * 
   > Cont, R. (2001). Empirical properties of asset returns: Stylized facts and statistical issues. Quantitative Finance, 1(2), 223–236.

  * Parkinson, M. (1980). The extreme value method for estimating the variance of the rate of return. Journal of Business, 53(1), 61–65.
  * Karpoff, J. M. (1987). The relation between price changes and trading volume: A survey. Journal of Financial and Quantitative Analysis, 22(1), 109–126.
  * Easley, D., López de Prado, M., & O’Hara, M. (2012). The microstructure of the stock market. Journal of Portfolio Management.
  * Andersen, T. G., & Bollerslev, T. (1998). Answering the skeptics: Yes, standard volatility models do provide accurate forecasts. International Economic Review, 39(4), 885–905.
  * Jegadeesh, N., & Titman, S. (1993). Returns to buying winners and selling losers: Implications for stock market efficiency. Journal of Finance, 48(1), 65–91.
  * Kim, J. H., & White, H. (2004). Consistent VK testing for structural breaks in GARCH models. Journal of Econometrics, 122(1), 225–250.
  * Caporale, G. M., & Plastun, A. (2018). Calendar anomalies in the cryptocurrency market. Finance Research Letters.



