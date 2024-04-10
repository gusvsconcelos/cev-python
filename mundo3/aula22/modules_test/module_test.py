""" Calculation """

import calculator

ADD = calculator.add
SUB = calculator.sub
MULT = calculator.mult
DIV = calculator.div
FACT = calculator.fact

MATH_OPTIONS = {
    0: 'soma',
    1: 'subtração',
    2: 'multiplicação',
    3: 'divisão',
    4: 'fatorial'
}


def display_menu():
    """ Display the menu for mathematical operations """

    print("""
Operações matemáticas disponíveis:
[0] Somar
[1] Subtrair
[2] Multiplicar
[3] Dividir
[4] Fatorial
          """)


def get_user_choice():
    """ Get user choice for mathematical operation """

    choice = int(input('Qual operação matemática você deseja fazer? '))

    return choice


def perform_operation(choice):
    """ Peform mathematical operation """

    if choice == 4:
        n = int(input('Digite um valor: '))

        print(f'O {MATH_OPTIONS[choice]} de {n} {FACT(n)}')
    else:
        a = int(input('Digite o primeiro valor: '))
        b = int(input('Digite o segundo valor: '))

        if choice == 0:
            print(f'A {MATH_OPTIONS[choice]} de {a} com {b} é {ADD(a, b)}')
        elif choice == 1:
            print(f'A {MATH_OPTIONS[choice]} de {a} com {b} é {SUB(a, b)}')
        elif choice == 2:
            print(f'A {MATH_OPTIONS[choice]} de {a} com {b} é {MULT(a, b)}')
        elif choice == 3:
            if choice == 0:
                print('Não é possivel realizar uma divisão por zero.')

            print(f'A {MATH_OPTIONS[choice]} de {a} com {b} é {DIV(a, b)}')


def main():
    """ Initialize program """

    display_menu()

    while True:
        choice = get_user_choice()

        if choice > 4:
            break

        perform_operation(choice)


if __name__ == '__main__':
    main()
