def find_max_min(numbers: list) -> tuple:
    """
    Finds the maximum and minimum values in the given list.
 
    :param numbers: The list of numbers.
    :return: A tuple containing the maximum and minimum values.
    :raises ValueError: If the list is empty.
    """
    if not numbers:
        raise ValueError("List is empty")
 
    maximum = minimum = numbers[0]
 
    for number in numbers[1:]:
        if number > maximum:
            maximum = number
        elif number < minimum:
            minimum = number
 
    return maximum, minimum
 
 
def test_find_max_min():
    assert find_max_min([1, 2, 3, 4, 5]) == (5, 1)
    assert find_max_min([10, 5, 7, 3, 8]) == (10, 3)
    assert find_max_min([-1, -2, -3, -4, -5]) == (-1, -5)
    assert find_max_min([0]) == (0, 0)
    try:
        find_max_min([])
        assert False  # This line should not be reached
    except ValueError:
        pass
 
 
if __name__ == '__main__':
    test_find_max_min()