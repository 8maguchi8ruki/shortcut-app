def post_tweet(form_value):
    import pyautogui as pg
    import webbrowser as web
    import time
    import pyperclip
    from flask import request


    # 値取得
    print(form_value)

    # 投稿
    web.open("https://twitter.com/compose/tweet")
    time.sleep(3)
    pyperclip.copy(form_value)
    pg.hotkey("ctrl", "v")
    time.sleep(1)
    pg.hotkey("ctrl","enter")
    pg.hotkey("ctrl","w")

