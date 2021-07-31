from selenium import webdriver
import pandas as pd

PATH = "D:\OneDrive\Development\Tools\chromedriver.exe"
url = "https://www.ptt.cc/bbs/Gossiping/index.html"


# 先定義點按同意的function，後續可以重複使用
def click_agree():
    # time.sleep(1)
    agree_btn = driver.find_element_by_xpath('/html/body/div[2]/form/div[1]/button')
    agree_btn.click()


# 使用driver.get()連到目標url: ptt八卦版後自動點擊同意
driver = webdriver.Chrome(PATH)
driver.get(url)
click_agree()

# 用css selector 取得所有文章的標題和文章連結，一一點進連結抓取發文時間，將文章標題和時間分別存成2個list
articles = driver.find_elements_by_css_selector(".r-ent .title a")
title_list = []
time_list = []
for item in articles:
    link = item.get_attribute("href")
    title_list.append(item.text)
    driver = webdriver.Chrome(PATH)
    driver.get(link)
    click_agree()
    time = driver.find_element_by_xpath('//*[@id="main-content"]/div[4]/span[2]').text
    time_list.append(time)
    driver.close()

# 使用pandas將資料轉存為DataFrame(也可以另存成csv檔)
output = pd.DataFrame({
    "標題": title_list,
    "時間": time_list
})
print(output)
