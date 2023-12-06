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
        return "為什麼機器人不會感冒？因為它有防毒軟體！"
    else:
        return "抱歉，我不太理解你的問題。"

# 測試
user_input = input("你: ")
response = chatbot(user_input)
print("機器人:", response)
