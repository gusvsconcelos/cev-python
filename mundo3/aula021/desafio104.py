""" Validating Input Data """


def header():
    """ Print the program header """

    print(f'{" DESAFIO 104 ":=^29}')


def read_int(prompt):
    """
    Read an integer from the user input.

        Args:
            prompt (str): The message prompt to display to the user.

        Returns:
            int: The integer entered by the user.

        If the input provided by the user is not a valid integer, an error
        message in red color is displayed, and None is returned.
    """

    while True:
        int_num = input(prompt)

        if not int_num.isnumeric():
            print(f'\033[91m {
                'ERRO! Valor inválido, por favor insira um número inteiro.'
            } \033[00m')
        else:
            return int(int_num)


def main():
    """ Initialize program """

    header()
    num = read_int('Digite um número: ')
    print(num)


if __name__ == "__main__":
    main()
