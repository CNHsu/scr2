import twstock
import matplotlib.pyplot as plt
from matplotlib import style,dates
from matplotlib.finance import candlestick_ohlc
import csv


style.use('ggplot')

sstock='2892'
stock= twstock.Stock(sstock)
stock.fetch_from(2017,8)
#f = open("2892.csv","w")
#w=csv.writer(f)
#w.writerow(stock.price)
#f.close()

#print(str(stock.price[-5:]))
#print(stock)

     
sdate=stock.date
sopen=stock.open
shigh=stock.high
slow=stock.low
sclose=stock.close
ssd=[]
#for i in range(len(sdate)):
#    if i == 0:
#        ssd.append(736542.0)
#    ssd.append(ssd[i]+1)

for i in range(len(sdate)):
    ssd.append(dates.date2num(sdate[i]))
print(ssd)

quotes = [tuple([ssd[i],
                 sopen[i],
                 shigh[i],
                 slow[i],
                 sclose[i]]) for i in range(len(sdate))]
print(quotes[0])
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1,title=sstock)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1,sharex=ax1)

ax1.plot(stock.date, stock.price, label='price')
ax1.plot(stock.date[9:], stock.moving_average(stock.price,10), label='price10')

candlestick_ohlc(ax1,quotes,colorup='r',colordown='black',width=0.6)
ax2.bar(stock.date, stock.transaction)
plt.show()

