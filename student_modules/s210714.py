def process(message: str) -> str:
    if message.startswith("計算"):
        calculation_expression = message[2:]
        try:
            result = eval(calculation_expression)
            return f"計算結果: {result}"
        except Exception as e:
            return f"計算失敗: {str(e)}"
    elif message == "debug":
        return "debug"
    elif message == "資訊社":
        return "讚"
    elif message == "資訊老師":
        return "帥"
    elif message == "資訊社的同學":
        return "棒"
    elif message == "資訊社的電腦":
        return "不好說"
    else:
        return "我不知道如何處理這個訊息"
