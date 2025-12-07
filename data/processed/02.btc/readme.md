# 비트코인 주가 예측 프로젝트: Processed Data

비트코인 주가 예측 프로젝트에서는 머신러닝을 위한 피처 엔지니어링 (Feature engineering)을 실시한다. 각 피처들은 논문에 언급되었거나 또는 주가 예측에 일반적으로 사용되는 것으로 선택하였다.

---

**1. 가격 기반 피처 (Price-based Features)**

 * log_return

   : 직전 시간 대비 로그 수익률

   $log \\_ return_t = \ln{\left(\dfrac{Close_t}{Close_{t-1}}\right)}$

 * abs_return
 
   : 로그 수익률의 절대값

   $abs \\_ return_t = \left|log \\_ return_t\right|$
  
 * high_low_range
 
   :	시가 대비 고저차 비율

   $high\\_low\\_range\_t = \dfrac{High\_t - Low\_t}{Open\_t}$ 
   
 * return_5
 
   :	지난 5시간 종가 변화율
  
   $return\\_5\_t = \dfrac{Close\_t - Close\_{t-4}}{Close\_{t-4}}$   
  
 * return_24

   : 지난 24시간 종가 변화율

   $return\\_24\_t = \dfrac{Close\_t - Close\_{t-23}}{Close\_{t-23}}$   
   
 * close_open
 
   : 시가 대비 종가 비율 변화

   $close\\_open_t = \dfrac{Close_t - Open_t}{Open_t}$
   
---

**2. 봉 기반 피처 (Candle-based Features)**

 * real_body	

   : 종가 − 시가의 절대값

   $real\\_body\_t = \left|Close\_t - Open\_t \right|$
  
 * upper_shadow
 
   :고가 − max(시가, 종가)

   $upper\\_shadow\_t = High\_t - \max(Open\_t, Close\_t)$

 * lower_shadow

   : min(시가, 종가) − 저가

   $lower\\_shadow\_t = \min(Open\_t, Close\_t) - Low\_t$
   
 * range

   : 봉의 전체 길이

   $range\_t = High\_t - Low\_t$
   
 * body_ratio

   : 봉 길이 대비 몸통 비율

   $body\\_ratio\_t = \dfrac{\left|Close\_t - Open\_t \right|}{HIgh_t-Low_t}$

 * upper_ratio
 
   : 봉 길이 대비 윗꼬리 비율

   $upper\\_ratio\_t = \dfrac{upper\\_shadow\_t}{range\_t}$
   
 * lower_ratio
 
   : 봉 길이 대비 아랫꼬리 비율

   $lower\\_ratio\_t = \dfrac{lower\\_shadow\_t}{range\_t}$
   
---
    
**3. 변동성 기반 피처 (Volatility-based Features)**

  * rolling_vol_24

   : 지난 24시간 로그수익률의 표준편차

   $rolling\\_vol\\_24\_t = \rm{std}(log\\_return\_{t-23:t})$
   
  * rolling_vol_168

   : 지난 168시간 로그수익률의 표준편차

   $rolling\\_vol\\_168\_t = \rm{std}(log\\_return\_{t-167:t})$
   
• Parkinson Volatility

  * parkinson_vol

   : 고저가 범위 기반 변동성 추정치

   $parkinson\\_vol\_t = \sqrt{\dfrac{1}{4 \ln(2)} \left( \ln{\left(\dfrac{High\_t}{Low\_t}\right)} \right)^2 }$

---

**4. 추세 기반 피처 (Trend-based Features)**
   
  * SMA_5

   : 지난 5시간 단순이동평균

   $SMA\\_5\_t = \dfrac{Close\_{t-4} + ... + Close\_{t}}{5}$
   
  * SMA_10

   : 지난 10시간 단순이동평균

   $SMA\\_10\_t = \dfrac{Close\_{t-9} + ... + Close\_{t}}{10}$
   
  * SMA_20

   : 지난 20시간 단순이동평균

   $SMA\\_20\_t = \dfrac{Close\_{t-19} + ... + Close\_{t}}{20}$


  * EMA_12

   : 지난 12시간 지수이동평균

   $EMA\\_12\_t = \dfrac{2}{13}Close\_t\ + (1 - \dfrac{2}{13})EMA\\_12\_{t-1}$

  * EMA_26

   : 지난 26시간 지수이동평균

   $EMA\\_26\_t = \dfrac{2}{27}Close\_t\ + (1 - \dfrac{2}{27})EMA\\_26\_{t-1}$
   
  * MACD

   : EMA_12와 EMA_26의 차이
   
   $MACD\_t = EMA\\_12\_t - EMA\\_26\_t$

---

**5. 모멘텀 기반 피처 (Momentum-based Features)**
  * RSI_14

   : 지난 14시간 상승 및 하락폭 비교
   
   $RSI\\_14\_t = 100 - \dfrac{100}{1 + RS\\_14\_t}$

   $RS\\_14\_t = \dfrac{avggain\\_14\_t}{avgloss\\_14\_t}$
   
   $change\_t = Close\_t - Close\_{t-1}$

   상승한 경우 $gain\_t = change\_t$

   하락한 경우 $loss\_t = change\_t$

   $avggain\\_14\_t = (gain\_{t-13} + ... + gain\_{t})/14$

   $avgloss\\_14\_t = (loss\_{t-13} + ... + loss\_{t})/14$

---
   
**6. 기술적 변동성 피처 (Technical Volatility features)**

  * TR

  : 현재 고저차 및 직전 시간 종가의 차이를 고려한 변동폭
    
  $TR\_t = \max(High\_t - Low\_t, |High\_t - Close\_{t-1}|, |Low\_t - Close\_{t-1}|)$

  * ATR_14

  : 지난 14 시간 평균 TR
    
  $ATR\\_{14}\_t = \dfrac{TR\_{t-13} + ... + TR\_t}{14}$

---

**7. 고차모멘트 피처 (Higher-Moment Features)**

  * skewness_24

  : 지난 24시간 로그 수익률 분포의 비대칭성

  $skewness\\_24\_(t) = \dfrac{E[(log\\_return-\mu)^3]}{\sigma^3}$

  * Kurtosis_24

  : 지난 24시간 로그 수익률 분포의 꼬리 두께께
    
  $kurtosis\\_24\_t = \dfrac{E[(log\\_return-\mu)^4]}{\sigma^4}$

---

**8. 참고문헌**

  > Cont, R. (2001). Empirical properties of asset returns: Stylized facts and statistical issues. Quantitative Finance, 1(2), 223–236.
  > Parkinson, M. (1980). The extreme value method for estimating the variance of the rate of return. Journal of Business, 53(1), 61–65.
  > Wilder, J. Welles. New concepts in technical trading systems. Greensboro, NC, 1978. 
  




