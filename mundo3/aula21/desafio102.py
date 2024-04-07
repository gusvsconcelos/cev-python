""" Factorial """


def header():
    """ Print the program header """

    print(f'{" DESAFIO 102 ":=^29}')


def factorial(n, show=False):
    """ -> Calculates the factorial of a number.
        :param n: The number to be calculated.
        :param show: (optional) Whether to show the calculation or not.
    """

    if show:
        res = 1
        for i in range(n, 0, -1):
            if i > 1:
                print(i, end=' x ')
            else:
                print(i, end=' = ')

            res *= i

        print(res)
    else:
        res = 1
        for i in range(n, 0, -1):
            res *= i

        print(res)


def factorial_input():
    """ This function will prompt the user to input the number for which to
        calculate the factorial.
    """

    num = int(input('Qual o número que você deseja calcular o factorial? '))
    show_calculation = str(input('Deseja ver o processo de calculo? [s/N] '))

    if show_calculation.lower() == 's':
        return factorial(num, show=True)

    return factorial(num)


def main():
    """ Initialize program """

    header()
    factorial_input()


if __name__ == "__main__":
    main()
