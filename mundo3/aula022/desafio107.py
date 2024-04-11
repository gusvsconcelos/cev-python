""" Price Manipulation """

from aula22_utils import moedas


def header():
    """ Display program header """

    print(f'{" DESAFIO 107 ":=^29}')


def main():
    """ Main program """

    header()
    num = float(input('Digite o preço: R$'))

    print(f'A metade de {num} é {moedas.half(num)}')
    print(f'O dobro de {num} é {moedas.double(num)}')
    print(f'Aumentando 10%, temos {moedas.increase(num, 10)}')
    print(f'Reduzindo 13%, temos {moedas.decrease(num, 13)}')


if __name__ == '__main__':
    main()
