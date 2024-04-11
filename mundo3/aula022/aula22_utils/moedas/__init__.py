""" Coins Manipulation """


def increase(c, p, f=False):
    """
    Increases the value 'c' by a percentage 'p'.

    Parameters:
    c (float): The initial value.
    p (float): The percentage increase.

    Returns:
    float: The increased value of 'c'.
    """

    c += c * p / 100

    if f:
        return coin(c)

    return c


def decrease(c, p, f=False):
    """
    Decreases the value 'c' by a percentage 'p'.

    Parameters:
    c (float): The initial value.
    p (float): The percentage decrease.

    Returns:
    float: The decreased value of 'c'.
    """

    c -= c * p / 100

    if f:
        return coin(c)

    return c


def half(c, f=False):
    """
    Divides the value 'c' by 2.

    Parameters:
    c (float): The initial value.

    Returns:
    float: Half of the value 'c'.
    """

    if f:
        return coin(c / 2)

    return c / 2


def double(c, f=False):
    """
    Doubles the value 'c'.

    Parameters:
    c (float): The initial value.

    Returns:
    float: Double of the value 'c'.
    """

    if f:
        return coin(c * 2)

    return c * 2


def coin(c):
    """
    Format the value of 'c' for currency.

    Parameters:
    c (float): The initial value.

    Returns:
    float: c formatted as a currency .
    """

    return f'R${c:.2f}'


def summary(c, i, d):
    """ Display a summary of all the operations """

    print('-' * 34)
    print(f'{"RESUMO DO VALOR":^34}')
    print('-' * 34)
    print(f'Preço analisado: \t{coin(c)}')
    print(f'Dobro do preço: \t{double(c, f=True)}')
    print(f'Metade do preço: \t{half(c, f=True)}')
    print(f'{i}% de aumento:  \t{increase(c, i, f=True)}')
    print(f'{d}% de redução: \t{decrease(c, d, f=True)}')
    print('-' * 34)
