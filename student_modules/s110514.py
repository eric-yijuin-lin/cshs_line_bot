def chatbot(message: str) -> str:
    message = message.lower()  # 轉換為小寫，以便不區分大小寫

    if "你好" in message:
        return "你好！有什麼我可以幫助你的嗎？"
    elif "吃飯了嗎" in message:
        return "還沒吃，你呢？"
    elif "感覺如何" in message:
        return "我是一個機器人，沒有感覺，但感謝你的關心！"
    elif "謝謝" in message:
        return "不客氣，隨時可以問我問題。"
    elif "天氣" in message:
        return "我不知道當前的天氣，但你可以使用一個天氣應用程式查詢。"
    elif "你喜歡什麼" in message:
        return "作為機器人，我沒有個人的喜好，但我喜歡幫助人們解答問題。"
    elif "告訴我一個笑話" in message:
        return "為什麼程序員喜歡喝茶？因為他們有優先TEA！"
    elif "今天有什麼新聞" in message:
        return "我不具備瀏覽最新新聞的能力，建議你查看新聞網站或應用。"
    elif "教我一個新單詞" in message:
        return "當然，新單詞是「effervescent」，表示冒泡的或充滿活力的。"
    elif "你喜歡喵星人還是汪星人" in message:
        return "雖然我不能有偏好，但我聽說喵星人和汪星人都很可愛！"
    elif "單身嗎" in message:
        return "我是一個機器人，所以我沒有感情或婚姻狀態。"
    elif "你覺得人工智慧會取代人類嗎" in message:
        return "這是一個很複雜的問題，人工智慧可以做很多事情，但人類的獨特性還是無法被完全替代。"
    elif "有什麼推薦的書籍嗎" in message:
        return "如果你喜歡科幻，我推薦《三體》；如果喜歡小說，則《囚鳥》是一本不錯的選擇。"
    elif message.startswith("計算"):
        try:
            calculation = re.search(r'計算(.+)', message).group(1)
            result = eval(calculation)
            return f"計算結果是: {result}"
        except Exception as e:
            return "無法執行計算。請確保輸入的數學表達式是正確的。"
    else:
        return "抱歉，我不太理解你的問題。"
