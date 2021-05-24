import FinanceDataReader as web
from datetime import date, timedelta
import matplotlib.pyplot as plt
import datetime

# %matplotlib inline

plt.figure(figsize=(15,13))
# from matplotlib import font_manager, rc
# # font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
# rc('font', family='AppleGothic')

today = date.today()
startday = date.today() - timedelta(720)
yesterday = date.today() - timedelta(1)
#startday = '3/14/2014'
#yesterday = '4/14/2016'
print(yesterday)

SEC = web.DataReader("036570", startday, yesterday)
# print(type(SEC))
print(SEC.tail(10))
# SEC['Close'].plot(figsize=(16,4))
plt.subplot(311)
SEC[:"2021-05-11"]['Close'].plot(figsize=(16,4), style='b') # 기간의 종가를 가져옴
plt.subplot(313)
SEC[:"2021-05-11"]["Volume"].plot(figsize=(16,4), style='g') # 기간의 거래량을 가져옴

plt.show()