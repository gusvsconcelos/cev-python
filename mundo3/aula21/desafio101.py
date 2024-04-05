""" Function to check the vote status of a user """

from datetime import date


def header():
    """ Print the program header """

    print(f'{" DESAFIO 101 ":=^29}')


def vote(age):
    """ This function will get as a parameter the age of a person
        and then will return their right to vote as optional, mandatory
        or denied relative to their age.
    """

    if 18 <= age <= 70:
        return 'VOTO OBRIGATÓRIO!'
    if age < 16:
        return 'VOTO NEGADO!'

    return 'VOTO OPCIONAL!'


def user_birth():
    """ This function will ask the user their birth year and then return their
        age.
    """

    birth_year = int(input('Em que ano você nasceu? '))
    user_age = date.today().year - birth_year

    return user_age


def main():
    """ Initialize program """

    header()
    user_age = user_birth()
    print(f'Você tem {user_age} anos. {vote(user_age)}')


if __name__ == "__main__":
    main()
