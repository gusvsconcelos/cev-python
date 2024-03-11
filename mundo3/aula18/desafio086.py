print(f'{" DESAFIO 086 ":=^29}')

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(3):
    for j in range(3):
        num = int(input(f'Digite o valor para [{i + 1}, {j + 1}]: '))
        matrix[i][j] = num
    
# print(matrix[0])
# print(matrix[1])
# print(matrix[2])

for i in range(3):
    for j in range(3):
        print(f'[{matrix[i][j]:^5}]', end=' ')
    print()