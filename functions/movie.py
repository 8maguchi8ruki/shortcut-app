from tkinter import font
from tkinter.constants import X
from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys as keys
import tkinter as tk


# Chrome起動
driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.smt-cinema.com/site/utsunomiya/index.html')
time.sleep(2)

# # tkinterから値取得
# def btn_click(event):
#     print(event)


# label_y = 10
# button_y = 10
# text_y = 30

# 作品名取得
movie_titles = driver.find_elements_by_xpath("//div[@class='inner clearfix']/h2")
movie_links = driver.find_elements_by_xpath("//p[@class='thumbnail']/a")

for (movie_title,movie_link)  in zip(movie_titles,movie_links):
    title_list = movie_title.text
    link_list = movie_link.get_attribute("href")

    # #####tkinterに出力#####
    # #ボタン
    # button = tk.Button(app, text="選択",foreground="#3cb371")
    # button.place(x=50,y=button_y)
    # button.bind("<ButtonPress>", btn_click)
    # # 作品名出力
    # label = tk.Label(app, text=movie_title.text,background="#3cb371",font="bold")
    # label.place(x=100,y=label_y)
    # txt = tk.Entry(width=50)
    # txt.place(x=100, y=text_y)
    # # リンクテキスト出力
    # txt.insert(tk.END,movie_link.get_attribute("href"))
    # label_y = label_y + 50
    # button_y = button_y + 50
    # text_y = text_y + 50



current_url = driver.current_url
if (current_url == "https://www.smt-cinema.com/site/utsunomiya/movie/detail\w"):
    # 予約可能時間
    ok_times = driver.find_elements_by_xpath("//div[@class='block ok']/div[@class='inner ok']/p[@class='time']/span")
    for ok_time in ok_times:
        print(ok_time.text)

time.sleep(2)


