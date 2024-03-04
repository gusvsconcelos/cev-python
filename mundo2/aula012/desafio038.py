print(f'{"=" * 8} DESAFIO 038 {"=" * 8}')

num_list = []

for i in range(2):
    num = int(input(f"Forneça o {i + 1}ª número: "))
    num_list.append(num)

print(num_list)

greater = max(num_list)
lesser = min(num_list)

if greater > lesser:
    print(f"O maior número é {greater} e o menor numero é {lesser}")
else:
    print(f"Os dois números são iguais")
