""" Counter """

from time import sleep


def header():
    """ Print the program header """

    print(f'{" DESAFIO 098 ":=^29}')


def counter(start, end, step):
    """ Prints a counter with the given parameters """

    if step < 0:
        step = abs(step)
    if step == 0:
        step = 1

    print("-=" * 24)
    if start < end:
        print(f'Contagem de {start} até {end} de {step} em {step}')
        for i in range(start, end + 1, + step):
            print(i, end=' ', flush=True)
            sleep(0.5)
        print('FIM!')
    else:
        print(f'Contagem de {start} até {end} de {step} em {step}')
        for i in range(start, end - 1, - step):
            print(i, end=' ', flush=True)
            sleep(0.5)
        print('FIM!')


def user_counter():
    """ Takes user inputs and use as a counter parameters """

    print("-=" * 24)
    print('Agora é a sua vez de personalizar a contagem!')

    start = int(input('INICIO: '))
    end = int(input('FIM: '))
    step = int(input('PASSO: '))

    return start, end, step


def main():
    """ Initalize program """

    header()
    counter(0, 10, 1)
    counter(10, 0, 2)
    start, end, step = user_counter()
    counter(start, end, step)


if __name__ == '__main__':
    main()
