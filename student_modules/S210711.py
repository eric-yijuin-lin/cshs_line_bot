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

    # New rule: Check if the message starts with "計算"
    if message.startswith("計算"):
        try:
            # Extract the mathematical expression and evaluate it
            calculation_result = eval(message[2:])
            return str(calculation_result)
        except Exception as e:
            return f"計算錯誤: {str(e)}"

    # Add a default return statement if none of the conditions match
    return "未知訊息"

# Example usage:
result = process("計算3 + 5")
print(result)

