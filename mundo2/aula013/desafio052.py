print(f'{"=" * 8} DESAFIO 052 {"=" * 8}')

# num = int(input('Digite um número: '))

# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             print(f'{num} não é um número primo')
#             break
#     else:
#         print(f'{num} é um número primo')
# else:
#     print(f'{num} não é um número primo')


# ==============================================
#               EXERCISE    REMAKE
# ==============================================

num = int(input("Digite um número: "))
total_divisible = 0

for i in range(1, num + 1):
    if num % i == 0:
        print("\033[33m", end=" ")
        total_divisible += 1
    else:
        print("\033[31m", end=" ")
    print(f"{i}", end=" ")
    print("\033[m", end=" ")

if total_divisible == 2:
    print(f"\n{num} é um número primo.")
else:
    print(f"\n{num} NÃO é um número primo.")
