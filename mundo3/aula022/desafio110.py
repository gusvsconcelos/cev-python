""" Price Manipulation 4 """

from aula22_utils import moedas


def header():
    """ Display program header """
    print(f'{" DESAFIO 110 ":=^29}')


def main():
    """ Main program """
    n = float(input('Digite o preço: R$'))

    moedas.summary(n, 8, 35)


if __name__ == '__main__':
    header()
    main()
