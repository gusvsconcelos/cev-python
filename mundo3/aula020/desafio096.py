""" Calculates plot area"""


def header():
    """ Print the program header. """

    print(f'{" DESAFIO 096 ":=^29}')


def calculate_area(width, length):
    """  Calculates the area from the plot dimensions received """

    return width * length


def get_dimensions():
    """ Get user input about the plot dimensions to calculate """

    print('  Controle de terrenos  ')
    print('------------------------')

    width = float(input('Largura do terreno: '))
    length = float(input('Comprimento do terreno: '))

    return width, length


def display_area(width, length, area):
    """ Display the area of the plot with appropriate units """

    print(f'> A área de um terreno de {width}x{length} é de {area}m²')


def main():
    """ Initialize program"""
    header()
    width, length = get_dimensions()
    area = calculate_area(width, length)
    display_area(width, length, area)


if __name__ == '__main__':
    main()
