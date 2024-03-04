print(f'{"=" * 8} DESAFIO 051 {"=" * 8}')

a = int(input("Primeiro termo da PA: "))
r = int(input("Razão da PA: "))

for i in range(10):
    termo = a + i * r
    print(termo, end=" ")
