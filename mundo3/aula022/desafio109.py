""" Price Manipulation 3 """

from aula22_utils import moedas


def header():
    """ Display program header """
    print(f'{" DESAFIO 109 ":=^29}')


def main():
    """ Main program """
    n = float(input('Digite o preço: R$'))

    print(f'A metade de {moedas.coin(n)} é {moedas.half(n, f=True)}')
    print(f'O dobro de {moedas.coin(n)} é {moedas.double(n, f=True)}')
    print(f'Aumentando 10%, temos {moedas.increase(n, 10, f=True)}')
    print(f'Reduzindo 13%, temos {moedas.decrease(n, 13, f=True)}')


if __name__ == '__main__':
    header()
    main()
