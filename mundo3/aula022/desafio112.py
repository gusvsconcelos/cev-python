""" Price Manipulation 6 """

from utilidadescev import moeda, dado


def header():
    """ Display program header """
    print(f'{" DESAFIO 112 ":=^29}')


def main():
    """ Main program """
    n = dado.money('Digite o preço: R$')

    moeda.summary(n, 8, 35)


if __name__ == '__main__':
    header()
    main()
