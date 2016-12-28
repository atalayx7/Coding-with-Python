'''
In mathematics, the Fibonacci numbers are the numbers in the
following integer sequence, called the Fibonacci sequence,
and characterized by the fact that every number
after the first two is the sum of the two preceding ones (Wikipedia)
Example:
    1, 1, 2, 3, 5 8, 13, 21, 34, 55, 89, ...

'''


def fibonacci(n):
    a, b = 0, 1
    while b < n:
        print(b, end=", ")

        a, b = b, a + b


fibonacci(100)
