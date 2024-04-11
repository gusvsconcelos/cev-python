""" Price Manipulation 2 """

from aula22_utils import moedas


def header():
    """ Display program header """

    print(f'{" DESAFIO 108 ":=^29}')


def main():
    """ Main program """

    header()
    n = float(input('Digite o preço: R$'))

    print(f'A metade de {moedas.coin(n)} é {moedas.coin(moedas.half(n))}')
    print(f'O dobro de {moedas.coin(n)} é {moedas.coin(moedas.double(n))}')
    print(f'Aumentando 10%, temos {moedas.coin(moedas.increase(n, 10))}')
    print(f'Reduzindo 13%, temos {moedas.coin(moedas.decrease(n, 13))}')


if __name__ == '__main__':
    main()
