Exercise 1
Suppose you have the function that calculates the sum of the even numbers in a list:



def sum_even_numbers(numbers):
    return sum(filter(lambda x: x % 2 == 0, numbers))


This function takes a list of integers as input, filters out the odd numbers using the filter function and a lambda expression, and returns the sum of the even numbers.



Use the parameterized library to write a parameterized test for the sum_even_numbers() function.



Test the sum_even_numbers() function with five different input lists:

[1, 2, 3, 4, 5]

[10, 20, 30, 40, 50]

[1, 3, 5, 7, 9]

[0, 2, 4, 6, 8]

[]



For each input list, you should also specify the expected output.



Tip: Use the @parameterized.expand decorator to create a separate test case for each set of input.

