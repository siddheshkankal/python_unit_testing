Exercise 4
Suppose you have the function that calculates the average of a list of numbers:



def average(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    if len(numbers) == 0:
        raise ValueError("List must not be empty")
    return sum(numbers) / len(numbers)


This function takes a list of numbers as input, checks if the input is a list using the isinstance function, and raises a TypeError if it is not. It then checks if the input list is empty using the len function, and raises a ValueError if it is. It then calculates the average of the numbers in the list and returns the result.



Use the parameterized library to write a parameterized test for the average() function.



Test the average() function with the following different input lists:

[1, 2, 3] -> 2

[10, 20, 30, 40] -> 25

[5] -> 5

[0, 0, 0] -> 0

[] -> None

["not a number"] -> None

["1", 2, 3] -> None

[None] -> None



Tip: You should use the parameterized.expand decorator to create a parameterized test. The decorator takes a list of tuples, each containing the input list and the expected output. The expand function expands each tuple into a separate test case with the input list and expected output as arguments.