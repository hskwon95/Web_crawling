
from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome('./chromedriver.exe')
driver.get("https://www.melon.com/chart/index.htm")
title=driver.find_elements_by_class_name('ellipsis.rank01')
how_many=30 #how many song to get

title2=[]
for i in title:
    title2.append(i.text)
del title2[how_many:]

singer=driver.find_elements_by_class_name('ellipsis.rank02')
singer2=[]
for i in singer:
    singer2.append(i.text)
del singer2[how_many:]

songTagList = driver.find_elements_by_id('lst50')

number=[]
for i in songTagList:
    number.append(i.get_attribute('data-song-no'))

LYRIC=[]
del number[how_many:]
for i in number:
    driver.get("https://www.melon.com/song/detail.htm?songId=" + i)
    lyric=driver.find_element_by_class_name("lyric")
    lyric2text = lyric.text
    LYRIC.append(lyric2text.replace("\n", " "))

year = "2021"
Lyricist = ["" for _ in range(how_many)]
df=pd.DataFrame({"title":title2,"lyric":LYRIC,"singer":singer2,"Lyricist":Lyricist})
df.to_excel(year+"_melon_TOP30.xlsx",  encoding='utf-8')

LYRIC=[]
for i in LYRIC:
    LYRIC.append(i.replace("\n",""))
