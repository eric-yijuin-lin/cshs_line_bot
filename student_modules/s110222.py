def process(message: str) -> str:
    if message == "debug":
        return message
    elif message == "你好臭":
        return "你好香"
    elif message == "你好":
        return "不好"
    elif message == "123456789+123456789=?":
        return "=246913578"
    elif message == "嗨":
        return "嗨"
    else:
        return "未知消息"

