# 股神巴菲特的老師 價值投資之父 葛拉漢的選股秘訣 淨營運資本法
# https://www.youtube.com/watch?v=OlnprlpHjQo&list=PLzr9EpvIZ0Grpd_W6d1A7CQvLh_yDveX0&index=1
import pandas as p 
from bs4 import BeautifulSoup
import requests

print("符合條件的股票:")
data = p.read_html('http://isin.twse.com.tw/isin/C_public.jsp?strMode=2', encoding='big5hkscs', header=0)[0]
data = p.DataFrame(data["有價證券代號及名稱"])
data = data["有價證券代號及名稱"].astype(str)

for x in data.iloc[1:977] :   #不一定是964 因為每天都可能有股票會上市或下市
    try:
        stockid = x[:4] #股票代號
    
        balance_url = "https://tw.stock.yahoo.com/quote/" + stockid +"/balance-sheet" #資產負債表的網址
        share_url = "https://tw.stock.yahoo.com/quote/"+ stockid +"/profile" #股數的網址
        price_url = "https://tw.stock.yahoo.com/quote/"+ stockid #股價的網址 

        def web(url):
            source = requests.get(url, headers={'Connection':'close'}) #連線到指定的網站
            soup = BeautifulSoup(source.content, 'lxml', from_encoding='utf-8') #讀取這個網頁的內容
            return soup #最終結果:回傳網頁內容

        balance = web(balance_url).find_all("span")[107:]
        for y in balance:
            if y.text == "流動資產":
                a = balance.index(y) + 4 #流動資產資料的位置
                asset = int(balance[a].string.replace(",", ""))*1000 #流動資產
    
            elif y.text == "總負債":
                b = balance.index(y) + 4 #總負債資料的位置
                liab = int(balance[b].string.replace(",", ""))*1000 #總負債

        div = web(share_url).find_all("div", class_="Py(8px) Pstart(12px) Bxz(bb)")
        share = int(div[16].string.replace(",", "")) #股數

        span = web(price_url).find_all("span")
        for z in span:
            if z.text == "成交":
                p = span.index(z) + 1 #股價資料的位置
                price = float(span[p].string) #股價
        
        #公式:股價<淨營運資本
        #淨營運資本 = (流動資產-總負債)/股數
        if(price < (asset-liab)/share):
            print(x)
    except:
        continue