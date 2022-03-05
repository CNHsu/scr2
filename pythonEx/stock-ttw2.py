################################
# stock optimize
#https://www.finlab.tw/Python新手教學：策略優化/
#https://ithelp.ithome.com.tw/articles/10205068
# need below coding... to have chinese
# coding=utf-8
import io
import time
import requests
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
#import matplotlib inline
plt.style.use('ggplot')

def crawl_price(stock_id,fname):
    now = int(datetime.datetime.now().timestamp())+86400
    url = "https://query1.finance.yahoo.com/v7/finance/download/" + stock_id + "?period1=0&period2=" + str(now) + "&interval=1d&events=history&crumb=hP2rOschxO0"

    response = requests.post(url)
    # option 1: save to file
    # already save to file?
    # skip the write csv to save time
    filename=fname.replace('/','_')+'.csv'
    print(filename)
    #with open(filename, 'w') as f:    # skip the write csv to save time
    #    f.writelines(response.text)   # skip the write csv to save time
    df = pd.read_csv(filename, index_col='Date', parse_dates=['Date'] )
        
    # option 2: save to system mem    
    #f = io.StringIO(response.text)
    #df = pd.read_csv(f, index_col='Date', parse_dates=['Date'] )

    return df

###################
# word stock index
#url = "https://finance.yahoo.com/world-indices/"
#response = requests.get(url)

#import io
#f = io.StringIO(response.text)
#dfs = pd.read_html(f)
dfs = pd.read_csv('mystock.csv',nrows=12)
print(dfs)
world_index = dfs

print(world_index)

##############################
# word stock info
stockinfo = {}
for symbol, name in zip(world_index['Symbol'], world_index['Name']):
    
    print(name)
    # ??? 2019/8/9 EGX no data? skip this info
    if (name == 'EGX 30 Price Return Index'):
        stockinfo['Top 40 USD Net TRI Index'] = crawl_price('^JN0U.JO','Top 40 USD Net TRI Index')
    else :
        stockinfo[name] = crawl_price(symbol,name)
 #   time.sleep(3.5) # need if read from web url


#########################################
# 收益率：代表股票在一天交易中的價值變化百分比

#plt.rcParams['axes.unicode_minus']=False
#fig = plt.figure(figsize=(10, 6))
#stockinfo['2886TW']['daily-return'] = stockinfo['2886TW']['Adj Close'].pct_change()
#stockinfo['2886TW']['daily-return'].plot(label="2886", kind='hist') 

#########################################
#使用seaborn的kde密度圖 
#fig = plt.figure(figsize=(10, 6))
#stockinfo['2886TW']['daily-return'] = stockinfo['2330TW']['Adj Close'].pct_change()
#sns.distplot(stockinfo['2886TW']['daily-return'].dropna(),bins=100, label="2886")

#########################################
#比較收益率關係，使用閃點圖
adjClose= {}
for name, price in stockinfo.items():
#    price['Adj Close']['2015':].plot(label=name)
         adjClose[name]=price['Adj Close']['2010':]
         print(name)
adjClose = pd.DataFrame(adjClose)
adjClose

print(adjClose)

#plt.rcParams['axes.unicode_minus']=False
adjClose_pct = adjClose.pct_change()
#sns.jointplot("2330TW","2886TW",adjClose_pct, kind="scatter")
#sns.jointplot("1513TW","2886TW",adjClose_pct, kind="scatter")
#sns.regplot('2330TW','2330TW',adjClose_pct)

###################################
# !!! below sharpe is not table
# you cannot plot with 'date'

#profit = adjClose_pct.mean()
#print("profit .....big is good")
#print(profit.sort_values())
#risk = adjClose_pct.std()
#print("RISK... small is good")
#print(risk.sort_values())
#sharpe = profit /risk * (252**0.5)
#print(" Sharp ... big is good")
#print(sharpe.sort_values())
###################################
# +rolling to change below to dataframe(table)
# and can plot with date
# !!!! no rolling sharpe is not table type

mean= adjClose_pct.rolling(252).mean()
risk = adjClose_pct.rolling(252).std()
sharpe= mean/risk *(252**0.5)
print(sharpe)
#print(" $$ Sharp ... big is good")
#print(sharpe.sort_values())

adjClose['2330TW'].plot()
#sharpe['2330TW'].plot(secondary_y=True)
sr = sharpe['2330TW'].dropna()
d=200
srsma = sr.rolling(d).mean()
srsmadiff =srsma.diff()
#sr.plot()
srsma.plot(secondary_y=True)
#srsmadiff.plot(secondary_y=True)
#########################################
# find buy or sell
buy = (srsmadiff > 0) & (srsmadiff.shift() < 0)
sell = (srsmadiff < 0) & (srsmadiff.shift() > 0)

(buy * 1).plot(secondary_y=True)
(sell * -1).plot(secondary_y=True)


#########################################
#同時比較公司 
# will take long time!!!
#sns.pairplot(adjClose_pct.dropna())

# pct_change() = (df_2492['Adj Close'][0] - df_2492['Adj Close'][1]) / df_2492['Adj Close'][1]

#twii = crawl_price("^TWII","TWN")
#twii.head()
#df_2886=crawl_price("2886.TW","bank")
#df_2330=crawl_price("2330.TW","TSMC")
#print(twii)

#twii.Close.plot()
#fig=plt.figure()
#df_2886['Adj Close']['2015':].plot(label="bank")
#df_2330['Adj Close']['2015':].plot(label='TSMC')
#plt.legend()

#for name, history in stockinfo.items():
#    history['Adj Close']['2015':].plot(label=name)
#stockinfo['2886TW'][']Close']['2015':].plot(label='2886')
#stockinfo['2886TW']['Adj Close']['2015':].plot(label='2886')





plt.legend() # define legend to have label show
plt.show()