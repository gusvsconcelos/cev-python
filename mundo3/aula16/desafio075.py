print("======== DESAFIO 075 ========")

numbers = (
    int(input("Digite o primeiro valor: ")),
    int(input("Digite o segundo valor: ")),
    int(input("Digite o terceiro valor: ")),
    int(input("Digite o quarto valor: ")),
    int(input("Digite o quinto valor: ")),
)

print(f"O número 9 apareceu {numbers.count(9)} vezes")
try:
    print(f"O número 3 apareceu pela primera vez no índice {numbers.index(3)}")
except ValueError:
    print("O número 3 não se encontra na tupla")

print("Os números pares são:", end=" ")
for num in numbers:
    if num % 2 == 0:
        print(num, end=" ")
