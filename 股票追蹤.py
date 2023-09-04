import pandas as p

p.options.display.max_rows = 100000
data = p.read_html('https://isin.twse.com.tw/isin/C_public.jsp?strMode=2', encoding='big5hkscs', header=0)[0]
data = data['有價證券代號及名稱'][1:967]

name = [] 
number = []
for stock in data:
    stockid = stock[:4]
    name.append(stock)
    number.append(stockid)
name = p.DataFrame(name, columns=['股票']).astype(str)
number = p.DataFrame(number, columns=['代號']).astype(int)

name.to_excel('上市股追蹤.xlsx', sheet_name='上市股', index=False)

with p.ExcelWriter('上市股追蹤.xlsx', mode='a', if_sheet_exists='overlay') as writer:
    number.to_excel(writer, sheet_name='上市股', index=False, startcol=1)