Exercise 5
Suppose you have the function that sorts a list of strings alphabetically:



def sort_strings(input_list):
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list")
    for item in input_list:
        if not isinstance(item, str):
            raise ValueError("All items must be strings")
    return sorted(input_list)


This function takes a list of strings as input, checks if the input is a list using the isinstance function, and raises a TypeError if it is not. It then checks if all items in the list are strings using a for loop, and raises a ValueError if any of them are not. It then sorts the list of strings alphabetically using the sorted function, and returns the sorted list.



Use the parameterized library to write a parameterized test for the sort_strings() function.



Test the sort_strings() function with the following different input lists:

["hello", "world"] -> ["hello", "world"]

["z", "a", "c"] -> ["a", "c", "z"]

[] -> []

["hello", 123] -> None

{"not": "a list"} -> None

["hello", None] -> None



Tip: You should use the parameterized.expand decorator to create a parameterized test. The decorator takes a list of tuples, each containing the input list and the expected output. The expand function expands each tuple into a separate test case with the input list and expected output as arguments.