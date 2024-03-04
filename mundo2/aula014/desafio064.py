print(f'{"=" * 8} DESAFIO 064 {"=" * 8}')

total_sum = 0
input_count = 0

while True:
    num = int(input("Digite um número [999 para parar]: "))

    if num == 999:
        break

    input_count += 1
    total_sum += num

print(f"Você digitou {input_count} números, e a soma entre eles é {total_sum}")
