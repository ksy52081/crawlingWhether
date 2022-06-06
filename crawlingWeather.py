# coding: utf-8
import requests
from bs4 import BeautifulSoup
response = requests.get('https://pythondojang.bitbucket.io/weather/observation/currentweather.html')

soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table', {'class' : 'table_develop3'})
##<table class = "table_develop3">

data = []

for tr in table.find_all('tr'): # find <tr>tag
    tds = list(tr.find_all('td')) # <td>tag list
    for td in tds:
        if(td.find('a')): #<a>tag
            point = td.find('a').text 
            temperature = tds[5].text
            humidity = tds[9].text
            data.append([point, temperature, humidity])
print(data)

with open('weather.csv', 'w') as file:
    file.write('point, temperature, humidity \n')
    for i in data:
        file.write('{0}, {1}, {2} \n'.format(i[0],i[1],i[2]))

# save as CSV file

get_ipython().run_line_magic('matplotlib', 'inline')

##################################################################
import pandas as pd 
import matplotlib as mpl 
import matplotlib.pyplot as plt 

df = pd.read_csv('weather.csv', index_col = 'point', encoding = 'euc-kr')

city_df = df.loc[['서울', '대전', '대구',  '부산']]
#city_df

# Windows font
font_name = mpl.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

# 차트 종류, 제목, 차트 크기, 범례, 폰트 크기 설정
ax = city_df.plot(kind='bar', title='날씨', figsize=(12, 4), legend=True, fontsize=12)
ax.set_xlabel('city', fontsize=12)          # x-axis
ax.set_ylabel('temp/humid', fontsize=12)     # y-axis
ax.legend(['temp', 'humid'], fontsize=12)    # 범례 지정

#city_df
