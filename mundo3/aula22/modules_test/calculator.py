""" Calculator """


def add(n, a):
    """
    Take two integers numbers as parameters (n and a) and return the result of 
    the sum between n and a.
    """

    return n + a


def sub(n, s):
    """
    Take two integers numbers as parameters (n and s) and return the result of 
    the subtraction between n and s.
    """

    return n - s


def mult(n, x):
    """
    Take two integer numbers as parameters (n and x) and return the result of the
    multiplication of n by x.
    """

    return n * x


def div(n, d):
    """
    Take two integer numbers as parameters (n and d) and return the result of the
    division of n by d.
    """

    return n / d


def fact(n):
    """
    Take an integer number as a parameter and return the result of it's
    factorial.
    """

    f = 1
    for c in range(n):
        f *= n - c
    return f
