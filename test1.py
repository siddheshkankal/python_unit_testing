import unittest
 
def add(x, y):
    return x + y

def divide(a, b):
    assert b != 0, "Division by zero is not allowed"
    return a / b

def max_min_diff(numbers):
    assert len(numbers) != 0, 'The input list cannot be empty.'
    return max(numbers) - min(numbers)

countries = ['POL', 'ENG', 'GER', 'USA', 'ITA']
is_italy = 'ITA' in countries

class TestAddition(unittest.TestCase):

    
    def test_add_positive_numbers(self):
        result = add(2, 3)
        self.assertEqual(result, 5)
 
    def test_add_negative_numbers(self):
        result = add(-2, -3)
        self.assertEqual(result, -5)

    # def test_division_numbers(self):
    #     result = divide(4, 0)
    #     self.assertEqual(result, 2)

    def test_division_numbers(self):
        result = divide(4, 2)
        self.assertEqual(result, 2)
    
    def test_countries(self):
        self.assertTrue(is_italy, 'Italy not found in the countries list.')

    def test_min_max(self):
        ans = max_min_diff([1,2])
        self.assertEqual(ans,1)

    
if __name__ == '__main__':
    unittest.main()
    
    
#     unittest framework - Intro
# The unittest framework, often referred to as "unittest" or "PyUnit," is a built-in testing framework in Python. It is inspired by the testing frameworks in other programming languages, such as JUnit for Java. unittest provides a structured way to write and execute test cases for your Python code, allowing you to ensure that your functions and classes behave as expected. Here's a description of the unittest framework in Python:

# Test Case Structure:

# The fundamental building block in unittest is a "test case." A test case is defined as a Python class that inherits from unittest.TestCase. Each test case class contains one or more test methods, which are regular Python methods whose names start with the word "test."

# Assertions:

# Within test methods, you use various assertion methods provided by unittest to check whether specific conditions are met. Common assertion methods include assertEqual, assertNotEqual, assertTrue, assertFalse, assertIsNone, assertIsNotNone, and many more. These assertions help you verify that your code produces the expected results.

# Test Discovery:

# unittest can automatically discover and run test cases and test methods in your codebase. This is especially useful when you have a large codebase with many test cases, as it simplifies the process of running tests.

# Test Suites:

# You can group multiple test cases into a test suite. A test suite is a collection of test cases that can be executed together. This allows you to organize and run related tests efficiently.

# SetUp and TearDown:

# unittest provides setUp and tearDown methods that can be defined in your test case classes. These methods are called before and after each test method, respectively, and are used for setting up and cleaning up resources needed for testing.

# Test Discovery and Test Execution:

# You can run tests using command-line tools like unittest test discovery and test runner. Alternatively, you can use third-party test runners such as pytest that offer more features and flexibility while still supporting unittest-style tests.

# Test Reporting:

# unittest provides basic test reporting, including information on which tests passed and which failed. However, for more advanced reporting and visualization, you might consider using third-party test reporting tools.

# Extensibility:

# You can extend the unittest framework by creating custom test runners, test loaders, and plugins to adapt it to your specific testing needs.



# # Here's a simple example of a unittest test case:
# In this example:

# We define a test case class TestAddition that inherits from unittest.TestCase.

# Within the test case class, we have two test methods: test_add_positive_numbers and test_add_negative_numbers.

# Each test method uses assertion methods like assertEqual to check the expected behavior of the add function.

# Finally, we use unittest.main() to run the tests.

# unittest is a powerful and versatile testing framework for Python, and it's commonly used for writing and running unit tests in Python projects. It's especially valuable for ensuring the correctness of individual functions and classes in your codebase.


# assert - Intro
# In Python, the assert statement is a debugging aid that is used to check whether a given condition is true or false, and it raises an AssertionError exception if the condition is false. The assert statement is typically used as a debugging tool during development to catch and diagnose issues in your code. Here's a description of the assert statement in Python:

# Syntax:

# The basic syntax of the assert statement is as follows: assert expression[, message]

# expression is the condition that you want to check. If it evaluates to False, Python raises an AssertionError exception.

# message (optional) is an additional message that you can provide to describe the assertion. This message is displayed when the assertion fails and can help you identify the problem.

# Usage:

# The primary use of the assert statement is to perform sanity checks and verify assumptions in your code. It's often used to validate that variables have expected values, preconditions are met, or that certain conditions are true during program execution.

# When to Use assert:

# assert statements are typically used in non-production code (e.g., during development and testing) to catch errors early in the development process. It's not intended for handling runtime errors in production code.

# The assert statements can be disabled globally using the -O (optimize) command-line switch when running Python. In optimized mode, assert statements are ignored, so they won't incur any runtime overhead in production code.

# Assertions with Debugging:

# When you encounter an AssertionError, it provides valuable information about the location in your code where the assertion failed and the message you provided. This helps you pinpoint and fix issues quickly during development.

# Documentation and Comments:

# While assert statements can serve as a form of documentation for the expected behavior of your code, it's generally better to use comments or docstrings to provide clear and detailed explanations of your code's assumptions and expectations.



# Example:

# def divide(a, b):
#     assert b != 0, "Division by zero is not allowed"
#     return a / b
 
# result = divide(10, 2)  # No assertion error
# result = divide(10, 0)  # Raises AssertionError with the message


# In this example, the assert statement checks whether the denominator b is not equal to zero before performing the division. If b is zero, an AssertionError is raised with the specified message.



# Remember that assert statements should not be used for error handling or validation in production code, as they can be disabled, and unexpected assertion failures can lead to unpredictable behavior. In production code, use proper error handling techniques like try and except for handling exceptional cases.