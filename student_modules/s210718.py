def process(message: str) -> str:
    if message == "debug":
        return "Debug 模式啟動"
    elif message == "同學":
        return "讚"
    elif message == "程式設計老師":
        return "帥"
    elif message == "福利社":
        return "棒"
    elif message == "4樓的電腦":
        return "不好說"
    elif message.startswith("計算"):
        # Extract the mathematical expression after "計算"
        expression = message[2:].strip()
        
        try:
            # Evaluate the mathematical expression
            result = eval(expression)
            return f"計算結果: {result}"
        except Exception as e:
            return f"計算失敗: {str(e)}"
    else:
        return "無法辨識的訊息"

# Example usage:
result = process("計算3 + 5")
print(result)
