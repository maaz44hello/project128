from bs4 import BeautifulSoup
import requests
import pandas as pd
page = requests.get("https://en.wikipedia.org/wiki/List_of_brown_dwarfs")
soup=BeautifulSoup(page.text,"html.parser")
star_table=soup.find_all("table")
table_rows=star_table[7].find_all("tr")
temp_list=[]


for tr_tags in table_rows:
    td_tags=tr_tags.find_all("td")
    row=[i.text.rstrip() for i in td_tags]
    temp_list.append(row)


Star_name = []
Distance = []
Mass = []
Radius = []

for i in range(1,len(temp_list)):
    Star_name.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])

df=pd.DataFrame(list(zip(Star_name,Distance,Mass,Radius)),columns=["Star_name","Distance","Mass","Radius"])
df.to_csv("dwarfs.csv")