print(f'{"=" * 8} DESAFIO 060 {"=" * 8}')

num = int(input("Digite um número: "))
res = 1

print(f"{num}! = ", end="")
while num > 0:
    if num == 1:
        print(f"{num} = {res}")
    else:
        print(f"{num} x ", end="")

    res *= num
    num -= 1

# With for loop
# print(f'{num}! = ', end='')
# for i in range(num, 0, -1):
#    if i == 1:
#        print(f'{i} = {res}')
#    else:
#        print(f'{i} x ', end='')
#
#    res *= i
