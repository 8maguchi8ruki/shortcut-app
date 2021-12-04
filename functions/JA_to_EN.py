def ja_to_en(form_value):

    from  selenium import webdriver
    import time
    from selenium.webdriver.common.keys import Keys
    from flask import request


    driver = webdriver.Chrome("./chromedriver")

    driver.get("https://www.deepl.com/ja/translator")


    time.sleep(1)

    print(form_value)

    search_box = driver.find_element_by_class_name("lmt__language_select__opener") 
    search_box.click()
    search_box = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[3]/div[3]/div[1]/div[2]/div[4]/div/div[3]/button[7]")   
    search_box.click()

    time.sleep(1)

    search_box = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[3]/div[3]/div[3]/div[1]/div[2]/div[1]/button/span/strong") 
    search_box.click()
    search_box = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[3]/div[3]/div[3]/div[3]/div[7]/div/div[3]/button[6]/div[1]")   
    search_box.click()

    search_box = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[3]/div[3]/div[1]/div[2]/div[2]/textarea")
    search_box.click()

    search_box.send_keys(form_value)

    time.sleep(100)
