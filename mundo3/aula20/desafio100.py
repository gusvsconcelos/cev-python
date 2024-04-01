""" Generate a list with random numbers and sum all the even numbers inside """

from random import randint
from time import sleep


def header():
    """ Print the program header """

    print(f'{" DESAFIO 100 ":=^29}')


def generate_numbers():
    """ Generate random numbers inside a list """

    random_numbers = [
        randint(1, 99),
        randint(1, 99),
        randint(1, 99),
        randint(1, 99),
        randint(1, 99)
    ]

    print('Sorteando 5 números:', end=' ')

    for n in random_numbers:
        print(n, end=' ', flush=True)
        sleep(0.5)

    print('FIM!')

    return random_numbers


def odd_sum(numbers):
    """ Sum all the odd numbers inside random_numbers list """

    sum_all_odds = 0

    for n in numbers:
        if n % 2 == 0:
            sum_all_odds += n

    print(f'Somando todos os valores pares de {numbers}, temos {sum_all_odds}')


def main():
    """ Initialize program """

    header()
    random_numbers = generate_numbers()
    odd_sum(random_numbers)


if __name__ == "__main__":
    main()
