from  selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("chromedriver")

driver.get("https://www.deepl.com/ja/translator")


time.sleep(1)
search_box = driver.find_element_by_class_name("lmt__language_select__opener") #言語
search_box.click()
search_box = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[3]/div[3]/div[1]/div[2]/div[4]/div/div[3]/button[5]")   #英語
search_box.click()
search_box = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[3]/div[3]/div[1]/div[2]/div[2]/textarea")
search_box.click()
search_box.send_keys("apple")

time.sleep(100)