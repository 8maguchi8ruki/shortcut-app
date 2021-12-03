import pyautogui as pg
import webbrowser as web
import time
import pyperclip
import sys
import tkinter


# 投稿
def post_tweet(text_value):
    web.open("https://twitter.com/compose/tweet")
    time.sleep(3)
    pyperclip.copy(text_value)
    pg.hotkey('ctrl', 'v')
    pg.hotkey("ctrl","enter")

# 値取得
def get_text():
    text_value = text.get()
    print(text_value)
    post_tweet(text_value)

###### GUI ######
root = tkinter.Tk()
root.title("Software Title")
root.geometry("1024x500")

# テキストボックス
text = tkinter.Entry(width=100)
text.place(x=100, y=100)

# ボタン
button = tkinter.Button(text=u'投稿',command=get_text)
button.pack(fill = 'x', padx=100 , pady=150)

root.mainloop()