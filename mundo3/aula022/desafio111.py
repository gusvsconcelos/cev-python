""" Price Manipulation 5 """

from utilidadescev import moeda


def header():
    """ Display program header """
    print(f'{" DESAFIO 111 ":=^29}')


def main():
    """ Main program """
    n = float(input('Digite o preço: R$'))

    moeda.summary(n, 8, 35)


if __name__ == '__main__':
    header()
    main()
