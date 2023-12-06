def process(message: str) -> str:
    # 判斷訊息的前兩個字是不是 "計算"
    if message.startswith("計算"):
        # 取得 "計算" 之後的部分
        expression = message[2:].strip()
        
        try:
            # 解析並計算數學運算
            result = eval(expression)
            return str(result)
        except Exception as e:
            # 如果有錯誤，回傳錯誤訊息
            return f"計算錯誤: {str(e)}"
    elif message == "debug":
        return message
    elif message == "資訊社":
        return "讚"
    elif message == "資訊老師":
        return "帥"
    elif message == "資訊社的同學":
        return "棒"
    elif message == "資訊社的電腦":
        return "不好說"
    elif message == "原神":
        return "啟動!!!"
    elif message == "今年多大了":
        return "剛滿18歲~"
    else:
        return "不理解你在說什麼"
