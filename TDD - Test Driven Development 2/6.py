Solution I:

def is_distinct(items):
    return len(items) == len(set(items))


Solution II:

from collections import Counter
 
def is_distinct(items):
    counts = Counter(items)
    return all(count == 1 for count in counts.values())