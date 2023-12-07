def max_min_diff(numbers):
    assert len(numbers) != 0,"numbers list can not be empty"
    return max(numbers) - min(numbers)
 
 
max_min_diff([])