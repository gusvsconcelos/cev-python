print(f'{"=" * 8} DESAFIO 042 {"=" * 8}')


def triangle():
    triangle_sides = []

    for i in range(3):
        while True:
            try:
                triangle_sides.append(int(input(f"Forneça o {i + 1}ª do triângulo: ")))
                break
            except ValueError:
                print("Por favor, insira um número válido.")

    x, y, z = sorted(triangle_sides)

    if x + y > z:
        print("É possivel formar um triângulo com os lados fornecidos")
        if x == y and x == z and y == z:
            print("É um triângulo equilátero")
        elif x == y or x == z or y == z:
            print("É um triângulo isósceles")
        else:
            print("É um triângulo escaleno")
    else:
        print("Não é possivel formar um triângulo com os lados fornecidos")


triangle()
