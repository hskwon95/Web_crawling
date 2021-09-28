
from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome('./chromedriver.exe')
year_list=[]
for i in range(1980,2021): #추출할 연도
    year_list.append(i)

how_many = 30  # 몇 개의 곡 뽑을껀지
for y_i in year_list:

    web_url="https://www.melon.com/chart/age/index.htm?chartType=YE&chartGenre=KPOP&chartDate="+str(y_i)
    driver.get(web_url)

    title = driver.find_elements_by_class_name('ellipsis.rank01')
    title2 = []
    for i in title:
        title2.append(i.text)
    del title2[how_many:]

    singer = driver.find_elements_by_class_name('ellipsis.rank02')
    singer2 = []
    for i in singer:
        singer2.append(i.text)
    del singer2[how_many:]

    songTagList = driver.find_element_by_id('tb_list').find_elements_by_class_name('btn.btn_icon_detail')

    number = []
    for i in songTagList:
        get_id=((i.get_attribute('onclick')).replace("melon.link.goSongDetail('", "")).replace("');","") #노래 id추출
        number.append(get_id)

    LYRIC = []
    del number[how_many:]
    for i in number:
        driver.get("https://www.melon.com/song/detail.htm?songId=" + i)
        lyric = driver.find_element_by_class_name("wrap_lyric")
        lyric2text=lyric.text
        LYRIC.append(lyric2text.replace("\n", " ")) # 줄 바꿈시 단어가 붙는 문제 해결

    Lyricist = ["" for _ in range(how_many)]
    df = pd.DataFrame({"title": title2, "lyric": LYRIC, "singer": singer2, "Lyricist": Lyricist})
    df.to_excel(str(y_i) + "_melon_TOP30.xlsx", encoding='utf-8')

    print(str(y_i)+"year done.")







