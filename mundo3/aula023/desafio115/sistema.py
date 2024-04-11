""" User Registration """

import menu
import pessoas


def header():
    """ Display exercise number header """

    print(f'{" DESAFIO 115 ":=^29}\n')


def main():
    """ Main program """

    header()

    while True:
        choice = menu.main_menu()

        # View users list
        if choice == 1:
            menu.view_users()
            pessoas.view()

        # Create a new user
        elif choice == 2:
            file_content = pessoas.read()
            user = pessoas.create_user(file_content)
            pessoas.write(user)

        # Delete the data file
        elif choice == 3:
            pessoas.delete()

        # Exit program
        elif choice == 4:
            menu.exit_program()
            break


if __name__ == '__main__':
    main()
