print(f'{" DESAFIO 082 ":=^29}')

numbers = []
odd_numbers = []
even_numbers = []

while True:
    num = int(input("Digite um número: "))
    numbers.append(num)

    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

    break_loop = input("Deseja continuar? [S/N] ")

    if break_loop.lower() == "n":
        break

print(f"Lista de números fornecidos: {numbers}")
print(f"Lista de números impares fornecidos: {odd_numbers}")
print(f"Lista de números pares fornecidos: {even_numbers}")
