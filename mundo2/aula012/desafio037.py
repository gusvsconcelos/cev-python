print(f'{"=" * 8} DESAFIO 037 {"=" * 8}')

print("\n=-=-=-=-=-= CONVERSOR DE BASES NUMÉRICAS =-=-=-=-=-=")

num = int(input("Digite um número: "))

print(
    """
[1] Binário
[2] Octal
[3] Hexadecimal
"""
)

base = int(input("Escolha uma base numérica para converter: "))

if base == 1:
    binario = ""
    while num > 0:
        resto = str(num % 2)
        binario = resto + binario
        num = num // 2

    print(binario)
elif base == 2:
    octal = ""
    while num > 0:
        resto = str(num % 8)
        octal = resto + octal
        num = num // 8

    print(octal)
elif base == 3:
    hex_letters = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    hexadecimal = ""
    while num > 0:
        resto = num % 16
        if resto >= 10:
            hexadecimal = hex_letters[resto] + hexadecimal
        else:
            hexadecimal = str(resto) + hexadecimal
        num = num // 16

    print(hexadecimal)
else:
    print("Escolha uma base numérica válida!")

    # Uma forma mais simples e fácil de resolver esse desafio seria usando as funções bin(), oct() e hex() do Python, porem, pelo beneficio da pratica e do aprendizado, optei por usar o método mais complicado
