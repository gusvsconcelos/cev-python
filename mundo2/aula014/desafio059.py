print(f'{"=" * 8} DESAFIO 059 {"=" * 8}')

num1 = int(input("Primeiro valor: "))
num2 = int(input("Segundo valor: "))

answer = 0
while answer != 5:
    print(
        """
    [ 1 ] somar

    [ 2 ] multiplicar

    [ 3 ] maior

    [ 4 ] novos números

    [ 5 ] sair do programa
    """
    )
    answer = int(input("Sua opção: "))

    if answer == 1:
        print(f"SOMA: {num1} + {num2} = {num1 + num2}")
    elif answer == 2:
        print(f"MULTIPLICAÇÃO: {num1} * {num2} = {num1 * num2}")
    elif answer == 3:
        print(f"MAIOR NÚMERO: {max(num1, num2)}")
    elif answer == 4:
        num1 = int(input(f"Primeiro valor [atual: {num1}]: "))
        num2 = int(input(f"Segundo valor [atual: {num2}]: "))
