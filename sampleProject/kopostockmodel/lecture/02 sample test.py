import FinanceDataReader as web # 주식정보 사용
from datetime import date, timedelta # 시간정보 사용
import matplotlib.pyplot as plt # 차트 도구
import datetime

# %matplotlib inline

plt.figure(figsize=(15,13)) # 차트의 너비, 높이
# from matplotlib import font_manager, rc
# # font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
# rc('font', family='AppleGothic')

today = date.today() # 오늘 날짜
startday = date.today() - timedelta(720) # 오늘 날짜로부터 약 2년 전
yesterday = date.today() - timedelta(1) # 어제 날짜
#startday = '3/14/2014'
#yesterday = '4/14/2016'
print(yesterday)

SEC = web.DataReader("036570", startday, yesterday) # 주식코드, 시작날짜, 어제날짜
# print(type(SEC))
print(SEC.tail(10)) # 하위 10개의 항목만 나타냄
# SEC['Close'].plot(figsize=(16,4))
plt.subplot(311) #3행 1열로 잡은 것 중 1번째
SEC[:"2021-05-11"]['Close'].plot(figsize=(16,4), style='b') # 기간의 종가를 가져옴
plt.subplot(313) #3행 1열로 잡은 것 중 3번째
SEC[:"2021-05-11"]["Volume"].plot(figsize=(16,4), style='g') # 기간의 거래량을 가져옴

plt.show()