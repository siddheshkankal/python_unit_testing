def cnt(string):
    words = string.split()
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for word in words:
        if word[0].lower() in vowels:
            count += 1
    return count
 
 
def test_cnt():
    assert cnt("dog cat egg") == 1, '"dog cat egg" failed'
    assert cnt("Apple igloo pet") == 2, '"Apple igloo pet" failed'
    assert cnt("file disk") == 0, '"file disk" failed'
    assert cnt("xyz") == 0, '"xyz" failed'
    assert cnt("") == 0, '"" failed'