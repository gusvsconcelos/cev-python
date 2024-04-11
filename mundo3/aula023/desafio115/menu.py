""" Menu """

from time import sleep
from colors import color as c


def main_menu():
    """ Display a menu with the available options for the user to chose """

    print(f'{c["end"]}{"=" * 50}')
    print('MENU PRINCIPAL'.center(50))
    print('=' * 50)

    print(f'{c["yellow"]} 1 ~ {c["blue"]}Ver pessoas cadastradas')
    print(f'{c["yellow"]} 2 ~ {c["blue"]}Cadastrar nova Pessoa')
    print(f'{c["yellow"]} 3 ~ {c["red"]}Deletar todos os dados [ATENÇÃO]')
    print(f'{c["yellow"]} 4 ~ {c["blue"]}Sair do Sistema{c["end"]}')

    print('=' * 50)

    while True:
        try:
            user_choice = int(input(f'{c["yellow"]}Sua opção:{c["green"]} '))

            while user_choice > 4:
                print(f'{c["red"]} ERRO! Digite uma opção válida. {c["end"]}')

                user_choice = int(
                    input(f'{c["yellow"]}Sua opção:{c["green"]} '))

            return user_choice

        except ValueError:
            print(f'{c["red"]} Insira um número inteiro. {c["end"]}')


def view_users():
    """ Display a header for the user list """

    print(f'{c["end"]}{"=" * 50}')
    print('PESSOAS CADASTRADAS'.center(50))
    print('=' * 50)


def new_user():
    """ Display a header for the create user menu """

    print(f'{c["end"]}{"=" * 50}')
    print('NOVO CADASTRO'.center(50))
    print('=' * 50)


def exit_program():
    """ Display a message when the program is closed """

    print(f'{c["end"]}{"=" * 50}')
    print('SAINDO DO PROGRAMA...'.center(50))
    print('=' * 50)

    sleep(2)

    print('Até logo!'.center(50))

    sleep(0.5)


def main():
    """ Initialize program """

    choice = main_menu()

    if choice == 1:
        view_users()
    elif choice == 2:
        new_user()


if __name__ == '__main__':
    main()
