print(f'{"=" * 8} DESAFIO 061 {"=" * 8}')

num = int(input("Digite o primeiro termo: "))
r = int(input("Razão da PA: "))

count = 10
while count > 0:
    print(f"{num}", end=" ")
    num += r
    count -= 1
