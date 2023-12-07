def calculate_median(numbers: list) -> float:
    """
    Calculates the median value of the given list of numbers.
 
    :param numbers: The list of numbers.
    :return: The median value.
    :raises ValueError: If the list is empty.
    """
    if not numbers:
        raise ValueError("List is empty")
    sorted_nums = sorted(numbers)
    length = len(sorted_nums)
 
    if length % 2 == 0:
        return (
            sorted_nums[length // 2 - 1] + sorted_nums[length // 2]
        ) / 2
    else:
        return sorted_nums[length // 2]
 
 
def test_calculate_median():
    assert calculate_median([1, 2, 3]) == 2
    assert calculate_median([4, 5, 6, 7]) == 5.5
    assert calculate_median([2, 1, 3]) == 2
    assert calculate_median([0, 0, 0, 0]) == 0
    try:
        calculate_median([])
        assert False  # This line should not be reached
    except ValueError:
        pass
 