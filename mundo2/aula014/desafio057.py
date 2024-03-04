print(f'{"=" * 8} DESAFIO 057 {"=" * 8}')

answer = ""

while answer.lower() != "m" and answer.lower() != "f":
    answer = input("Qual o seu sexo? [M/F]: ")

    if answer.lower() != "m" and answer.lower() != "f":
        print("Valor inválido, por favor tente novamente.")
    elif answer.lower() == "m":
        print("Tu é macho")
    else:
        print("Tu é muie")
