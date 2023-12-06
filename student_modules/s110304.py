from sympy import sympify

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
        expression = message[2:].strip()  # 取得計算表達式
        try:
            result = sympify(expression)  # 使用 sympy 套件計算
            return f"計算結果：{result}"
        except Exception as e:
            return f"計算失敗：{str(e)}"
    else:
        return "抱歉，我不知道您在公沙小"
