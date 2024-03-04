print("======== DESAFIO 066 ========")

total_inputs = 0
total_sum = 0
while True:
    if total_inputs == 0:
        num = int(input("Digite um número: "))
    else:
        num = int(input("Digite mais um número: "))

    if num == 999:
        break

    total_sum += num
    total_inputs += 1

print(
    f"O total de números digitados foi: {total_inputs}, e a soma de todos os números é: {total_sum}"
)
