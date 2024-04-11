""" User Registration """

from time import sleep
from colors import color as c


def read():
    """ 
    Read the users data file and return its content as a parameter for the
    create_user() method.

    If no file are found, None is returned.
    """

    try:
        file = 'users.txt'

        with open(file, 'r', encoding='utf-8') as file:
            content = file.read()

        return content

    except FileNotFoundError:
        print(f'{c["red"]} O arquivo não foi encontrado. {c["end"]}')

        return None


def create_user(users):
    """
    Receive the content from the users data file and proceed to add a new user
    for the existent ones, then return it to the write() method to update the
    user data file.

    If no existent content are available, it creates it and return for the
    write() method to be written on a new file.
    """

    name = None
    age = None

    while True:
        name = input(f'{c["end"]}NOME:{c["green"]} ').strip()

        if name and not name.isnumeric():
            break

        print(f'{c["red"]} Insira um nome válido. {c["end"]}')

    while True:
        try:
            age = int(input(f'{c["end"]}IDADE:{c["green"]} '))

            if isinstance(age, int):
                break

        except ValueError:
            print(f'{c["red"]} Insira apenas valores inteiros. {c["end"]}')

    try:
        users += f'{name:<40} {age} anos\n'

        return users

    except TypeError:
        users = f'{name:<40} {age}\n'

        return users

    finally:
        print(f'{c["green"]} Usuário cadastrado. {c["end"]}')


def write(users):
    """
    Takes the content of the users data file with the new users already added
    then overwrite the older file with an updated one.
    """

    new_file = 'users.txt'

    with open(new_file, 'w', encoding='utf-8') as file:
        file.write(users)

    return new_file


def delete():
    """ DELETE ALL USER DATA [BE CAREFUL] """

    file = 'users.txt'

    with open(file, 'r+', encoding='utf-8') as file:
        file.truncate(0)

    print(f'{c["red"]} Deletando dados... {c["end"]}', flush=True)
    sleep(2)
    print(f'{c["red"]} Todos os dados deletados {c["end"]}')
    sleep(1)


def view():
    """ Display the list of registred users """

    file = 'users.txt'

    with open(file, 'r', encoding='utf-8') as file:
        user_list = file.read()

    print(user_list)


def main():
    """ Initialize program """

    file_content = read()
    new_users = create_user(file_content)
    write(new_users)
    view()


if __name__ == '__main__':
    main()
