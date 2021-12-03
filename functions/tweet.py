def post_tweet():
    import pyautogui as pg
    import webbrowser as web
    import time
    import pyperclip
    from flask import request


    # 値取得
    text_value = request.form.get("text")
    print(text_value)

    # 投稿
    web.open("https://twitter.com/compose/tweet")
    time.sleep(3)
    pyperclip.copy(text_value)
    pg.hotkey("ctrl", "v")
    time.sleep(1)
    pg.hotkey("ctrl","enter")
    pg.hotkey("ctrl","w")

