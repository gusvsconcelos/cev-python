print(f'{" DESAFIO 081 ":=^29}')

numbers = []
counter = 1

while True:
    num = int(input("Digite um número: "))
    numbers.append(num)
    stop_loop = input("Deseja continuar? [S/N] ")

    if stop_loop.lower() == "n":
        break

    counter += 1

for i in range(len(numbers)):
    for j in range(len(numbers) - 1):
        if numbers[j] < numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(f"Você digitou {counter} números")
print(f"Os valores em ordem decrescente são {numbers}")
print(
    "O valor 5 se encontra na lista"
    if 5 in numbers
    else "O valor 5 não se encontra na lista"
)
