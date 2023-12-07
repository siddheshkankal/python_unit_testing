Solution I:

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


Solution II:

from functools import reduce
import operator
 
 
def factorial(n):
    return reduce(operator.mul, range(1, n+1), 1)