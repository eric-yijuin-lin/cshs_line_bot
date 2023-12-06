def process(message: str) -> str:
    if message == "debug":
        return message
    elif message == "啊啊啊啊啊啊":
        return "花惹發"
    elif message == "怎樣啦":
        return "ㄜ，你是怎樣"
    elif message == "不爽啦幹":
        return "喔是喔"
    elif message == "唉":
        return "唉"
    elif message.startswith("計算"):
        # 提取計算表達式並計算結果
        expression = message[2:].strip()  # 去掉前兩個字"計算"，並去除首尾空格
        try:
            result = eval(expression)  # 使用eval函數計算表達式
            return str(result)
        except Exception as e:
            return f"計算錯誤：{str(e)}"
    else:
        return "抱歉，我不知道您在公沙小"

