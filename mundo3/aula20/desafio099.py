""" The greater number """

from time import sleep


def header():
    """ Print the program header """

    print(f'{" DESAFIO 099 ":=^29}')


def greater_num(* num):
    """ Print the greater num of a given tuple """
    print('-=' * 25)
    print('Analisando os valores passados...')

    sleep(2)

    for n in num:
        print(n, end=' ', flush=True)
        sleep(0.5)

    print(f'\nForam passados {len(num)} valores ao todo')
    print(f'O maior valor informado foi {max(num)}')


def main():
    """ Initialize program """

    header()
    greater_num(10, 20, 5, 3)
    greater_num(65, 15, 30)
    greater_num(40, 88)
    greater_num(1)


if __name__ == "__main__":
    main()
