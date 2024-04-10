""" Coins Manipulation """


def increase(c, p):
    """
    Increases the value 'c' by a percentage 'p'.

    Parameters:
    c (float): The initial value.
    p (float): The percentage increase.

    Returns:
    float: The increased value of 'c'.
    """

    c += c * p / 100
    return c


def decrease(c, p):
    """
    Decreases the value 'c' by a percentage 'p'.

    Parameters:
    c (float): The initial value.
    p (float): The percentage decrease.

    Returns:
    float: The decreased value of 'c'.
    """

    c -= c * p / 100
    return c


def half(c):
    """
    Divides the value 'c' by 2.

    Parameters:
    c (float): The initial value.

    Returns:
    float: Half of the value 'c'.
    """

    return c / 2


def double(c):
    """
    Doubles the value 'c'.

    Parameters:
    c (float): The initial value.

    Returns:
    float: Double of the value 'c'.
    """

    return c * 2
