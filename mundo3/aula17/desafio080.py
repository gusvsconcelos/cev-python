print(f'{" DESAFIO 080 ":=^29}')

numbers = []

for i in range(5):
    num = int(input("Digite um valor: "))

    if i == 0 or num > numbers[-1]:
        numbers.append(num)
        print(f"O valor {num} foi adicionado no final da lista")
    else:
        for j in range(len(numbers)):
            if num <= numbers[j]:
                numbers.insert(j, num)
                print(f"O valor {num} foi adicionado na posição {j}")
                break

print(numbers)
