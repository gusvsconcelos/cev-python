print("======== DESAFIO 072 ========")

numbers = (
    "zero",
    "um",
    "dois",
    "três",
    "quatro",
    "cinco",
    "seis",
    "sete",
    "oito",
    "nove",
    "dez",
    "onze",
    "doze",
    "treze",
    "catorze",
    "quinze",
    "dezesseis",
    "dezessete",
    "dezoito",
    "dezenove",
    "vinte",
)

num = -1
while num < 0 or num > 20:
    num = int(input("Dite um número entre 0 e 20: "))

    if num < 0 or num > 20:
        print("Valor inválido, tente novamente: ")

print(f"Você digitou o número {numbers[num]}")
