print(f'{"=" * 8} DESAFIO 048 {"=" * 8}')

sum_odd_3s = 0
for i in range(1, 500):
    if i % 2 != 0 and i % 3 == 0:
        sum_odd_3s += i
print(sum_odd_3s)
