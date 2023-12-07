Solution I:

def filter_ge_four_char(words):
    result = []
    for word in words:
        if len(word) >= 4:
            result.append(word)
    return result


Solution II:

def filter_ge_four_char(words):
    return [word for word in words if len(word) >= 4]