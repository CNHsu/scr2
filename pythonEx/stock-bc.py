################################
# stock optimize
#https://www.finlab.tw/Python新手教學：策略優化/
#https://ithelp.ithome.com.tw/articles/10205068
import io
import time
import requests
import pandas as pd
import datetime
import matplotlib.pyplot as plt
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
url = "https://finance.yahoo.com/world-indices/"
response = requests.get(url)

import io
f = io.StringIO(response.text)
dfs = pd.read_html(f)
world_index = dfs[0]

print(world_index)

##############################
# word stock info
world_index_history = {}
for symbol, name in zip(world_index['Symbol'], world_index['Name']):
    
    print(name)
    # ??? 2019/8/9 EGX no data? skip this info
    if (name == 'EGX 30 Price Return Index'):
        world_index_history['Top 40 USD Net TRI Index'] = crawl_price('^JN0U.JO','Top 40 USD Net TRI Index')
    else :
        world_index_history[name] = crawl_price(symbol,name)
 #   time.sleep(3.5) # need if read from web url



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
for name, history in world_index_history.items():
    history.Close.plot()


plt.show()