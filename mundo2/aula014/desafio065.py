print(f'{"=" * 8} DESAFIO 065 {"=" * 8}')

greater = 0
lesser = 10
total_sum = 0
answer = "s"
input_count = 0

while answer.lower() == "s":
    num = int(input("Digite um número: "))
    total_sum += num
    if num > greater:
        greater = num
    if num < lesser:
        lesser = num
    input_count += 1
    answer = input("Você deseja continuar? [S/N] ")

print(
    f"A média de valores digitados foi {total_sum / input_count}, o maior número digitado foi {greater}, o menor foi {lesser}"
)
