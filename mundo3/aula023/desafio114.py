""" Site Connect Request """

import requests


def header():
    """ Print the program header """

    print(f'{" DESAFIO 114 ":=^29}')


def check_website_connection(url):
    """
    Tries to connect to a given website and print the result of the connection
    on the user console.

    args: url (any given website url)
    """

    try:
        response = requests.get(url)

        if response.status_code == 200:
            print(f'\033[92m Consegui me conectar ao site <{url}>! \033[00m')
    except requests.exceptions.RequestException:
        print(f'\033[91m Não consegui me conectar ao site <{url}>. \033[00m')


def main():
    """ Initialize program """
    check_website_connection('https://www.google.com.br/')


if __name__ == '__main__':
    main()
