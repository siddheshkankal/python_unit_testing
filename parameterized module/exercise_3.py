Exercise 3
Suppose you have the function that creates a list of tuples containing each integer and its square:



def square_pairs(numbers):
    return [(x, x**2) for x in numbers]


This function takes a list of integers as input and returns a list of tuples containing each integer and its square. We use a list comprehension to create the list of tuples.



Use the parameterized library to write a parameterized test for the square_pairs() function.



Test the square_pairs() function with five different input lists:

[1, 2, 3, 4, 5] -> [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

[-1, 0, 1] -> [(-1, 1), (0, 0), (1, 1)]

[] -> []

[2**31-1] ->  [(2**31-1, (2**31-1)**2)



For each input list, you should also specify the expected output.



Tip: Use the @parameterized.expand decorator to create a separate test case for each set of input.

