Solution I:

def map_longest(words):
    if not words:
        return 0
    lengths = []
    for word in words:
        lengths.append(len(word))
    return max(lengths)


Solution II:

def map_longest(words):
    return max(len(word) for word in words) if words else 0