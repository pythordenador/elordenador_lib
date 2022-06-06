
def replace(text,sel ,separator):
    splitted = text.split(separator)
    message = ""
    for i in splitted:
        message = message + i + sel
    rep = len(sel)
    return message[:len(message)-rep]
