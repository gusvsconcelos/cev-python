print(f'{" DESAFIO 087 ":=^29}')

matrix: list[int] = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
odd_sum: int = 0
third_column_sum: int = 0

for i in range(3):
    for j in range(3):
        num: int = int(input(f"Digite o valor para [{i + 1}, {j + 1}]: "))
        matrix[i][j] = num

        if num % 2 == 0:
            odd_sum += num
        if j == 2:
            third_column_sum += num

# second_line_max = max(matrix[1])

second_line_max: int = matrix[1][0]

for num in matrix[1]:
    if num > second_line_max:
        second_line_max = num

# print(matrix[0])
# print(matrix[1])
# print(matrix[2])

for i in range(3):
    for j in range(3):
        print(f"[{matrix[i][j]:^5}]", end=" ")
    print()

print(f"A soma de todos os valores pares digitados: {odd_sum}")
print(f"A soma dos valores da terceira coluna: {third_column_sum}")
print(f"O maior valor da segunda linha: {second_line_max}")
