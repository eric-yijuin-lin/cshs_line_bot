def process(message: str) -> str:
    if message == "debug":
        return message
    if message == "資訊社":
        return "讚"
    if message == "資訊老師":
        return "帥"
    if message == "資訊社的同學":
        return "棒"
    if message == "資訊社的電腦":
        return "不好說"
    if message.startswith("計算"):
        # 提取 "計算" 之後的數學運算表達式
        expression = message[2:].strip()
        
        try:
            # 嘗試計算數學運算
            result = eval(expression)
            return str(result)
        except Exception as e:
            # 如果計算失敗，返回錯誤消息
            return f"計算失敗: {e}"
    if message == "你好":
        return "12"

# 使用例子
result = process("計算 2 + 3 * 5")
print(result)

