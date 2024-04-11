""" Validating Input Data 2 """


def header():
    """ Print the program header """

    print(f'{" DESAFIO 113 ":=^29}')


def read_float(prompt):
    """
    Read a float number from the user input.

    Args:
        prompt (str): The message prompt to display to the user.

    Returns:
        float: The float number entered by the user.

    If the input provided by the user is not a valid float, an error
    message in red color is displayed, and the user is asked to input a valid
    float number again.
    """

    while True:
        try:
            float_num = float(input(prompt))
            return float_num
        except ValueError:
            print('\033[91m ERRO! Insira um número real. \033[00m')
        except KeyboardInterrupt:
            print('\033[91m O usúario preferiu não digitar. \033[00m')
            float_num = 0
            return float_num


def read_int(prompt):
    """
    Read an integer from the user input.

    Args:
        prompt (str): The message prompt to display to the user.

    Returns:
        int: The integer entered by the user.

    If the input provided by the user is not a valid integer, an error
    message in red color is displayed, and the user is asked to input a valid
    integer again.
    """

    while True:
        try:
            int_num = int(input(prompt))
            return int_num
        except ValueError:
            print('\033[91m ERRO! Insira um número inteiro válido. \033[00m')
        except KeyboardInterrupt:
            print('\033[91m O usúario preferiu não digitar. \033[00m')
            int_num = 0
            return int_num


def main():
    """ Initialize program """

    header()

    int_num = read_int('Digite um número inteiro: ')
    float_num = read_float('Digite um número real: ')

    print(f'O valor inteiro foi {int_num} e o valor real foi {float_num}')


if __name__ == "__main__":
    main()
