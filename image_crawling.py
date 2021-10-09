from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os


def crawling_img(keyword, how_many,save_path):
    driver = webdriver.Chrome('C:/Users/hyunsong/Desktop/Web_crawling/chromedriver.exe')
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
    elem = driver.find_element_by_name("q")
    elem.send_keys(keyword)
    elem.send_keys(Keys.RETURN)

    SCROLL_PAUSE_TIME = 1
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")  # 브라우저의 높이를 자바스크립트로 찾음

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 브라우저 끝까지 스크롤을 내림
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                driver.find_element_by_css_selector(".mye4qd").click()
            except:
                break
        last_height = new_height
    imgs = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
    print("!!",len(imgs))
    count = 1
    for img in imgs:
        try:
            img.click()
            time.sleep(2)
            imgUrl = driver.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img').get_attribute("src")
            urllib.request.urlretrieve(imgUrl, save_path+str(count) + ".jpg")
            if count == how_many:
                break
            count = count + 1
        except:
            pass

    driver.close()
    print("done.")

if __name__ == "__main__":
    keyword_list = ["라넌큘러스 꽃다발","자나 장미 꽃다발","작약 꽃다발","프리지아 꽃다발","해바라기 꽃다발","델피늄 꽃다발","수국 꽃다발"]
    how_many = 300
    save_path = "C:/Users/hyunsong/Desktop/Web_crawling/result/"
    for keyword in keyword_list:
        os.makedirs(save_path+keyword)
        crawling_img(keyword, how_many, save_path+keyword+"/")
