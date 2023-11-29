def process(message: str) -> None:
    if message == "debug":
        return message
    if message == "指令方塊":
        return "command block"
    if message == "透明方塊":
        return "barrier"
    if message == "原神":
        return "啟動"
    if message == "傳送":
        return "tp"
    if message == "死亡":
        return "kill"
