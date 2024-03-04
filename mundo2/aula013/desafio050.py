print(f'{"=" * 8} DESAFIO 050 {"=" * 8}')

pair_sum = 0
for i in range(6):
    num = int(input(f"Digite o {i + 1}ª número: "))
    if num % 2 == 0:
        pair_sum += num
print(pair_sum)
