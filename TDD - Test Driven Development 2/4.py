Solution I:

def count_string(items):
    total = 0
    for item in items:
        if isinstance(item, str):
            total += 1
    return total


Solution II:

def count_string(items):
    return sum(isinstance(item, str) for item in items)