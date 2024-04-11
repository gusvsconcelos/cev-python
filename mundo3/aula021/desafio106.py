""" Interactive Helping System """


def header():
    """ Print the program header """

    print(f'{" DESAFIO 106 ":=^29}')


def interactive_helper(func):
    """
    Takes the user input (str) of a chosen built-in function as a parameter and
    return the help() method page of the module, function, class, keyword, or 
    documentation topic printed on the console.
    """
    if func == '':
        return print('Por favor, insira o nome de uma função válida.')

    return help(func)


def main():
    """ Initialize program """

    header()

    while True:
        help_func = input("Help: ")

        if help_func.upper() == 'FIM':
            break

        interactive_helper(help_func)


if __name__ == "__main__":
    main()
