print(f'{" DESAFIO 085 ":=^29}')

numbers = [[], []]

for i in range(7):
    num = int(input(f'Digite o {i + 1}ª valor: '))
    if num % 2 == 0:
        numbers[0].append(num)
    else:
        numbers[1].append(num)

print(f'Números pares: {numbers[0]}')
print(f'Números impares: {numbers[1]}')
