Exercise 2
Suppose you have the function that reverses a string:



def reverse_string(input_str):
    return input_str[::-1]


This function takes a string as input and returns the reverse of the string using slicing.



Use the parameterized library to write a parameterized test for the reverse_string() function.



Test the reverse_string() function with five different input lists:

"hello"

"python"

"racecar"

"12345"

"" (empty string)



For each input list, you should also specify the expected output.



Tip: Use the @parameterized.expand decorator to create a separate test case for each set of input.