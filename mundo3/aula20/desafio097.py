""" Print a message in the center of two lines with adaptative length """


def header():
    """Print a header for the program"""
    print(f'{" DESAFIO 097 ":=^29}')


def write(msg):
    """Write a message inside two lines with adaptative length"""
    print("~~" * len(msg))
    print(msg.center(len(msg) * 2))
    print("~~" * len(msg))


def main():
    """Initialize program"""
    header()

    while True:
        msg = input("Escreva uma mensagem: ")
        write(msg)

        stop_loop = input("Deseja escrever outra? [S/n] ")

        if stop_loop in "Nn":
            break


if __name__ == "__main__":
    main()

# def escreva(msg):
#     print('~~' * len(msg))
#
#
# msg = 'Olá, Mundo!'
#
# escreva(msg)
# print(msg.center(len(msg) * 2))
# escreva(msg)
#
# msg = 'Curso em Vídeo'
#
# escreva(msg)
# print(msg.center(len(msg) * 2))
# escreva(msg)
