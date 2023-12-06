def process(message: str) -> str:
    if message == "debug":
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

# 測試函數
test_message = "資訊社的同學"
result = process(test_message)
print(result)
