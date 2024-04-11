print("======== DESAFIO 078 ========")

numbers = []

for i in range(5):
    num = int(input("Digite um valor: "))
    numbers.append(num)

greater_num = numbers[0]
lesser_num = numbers[0]

for i in range(len(numbers)):
    if numbers[i] > greater_num:
        greater_num = numbers[i]
    elif numbers[i] < lesser_num:
        lesser_num = numbers[i]

print(numbers)
print(
    f"O maior valor da lista foi {greater_num} na posição {numbers.index(greater_num)}"
)
print(f"O menor valor da lista foi {lesser_num} na posição {numbers.index(lesser_num)}")
