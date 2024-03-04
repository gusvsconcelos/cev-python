print("======== DESAFIO 079 ========")

numbers = []
while True:
    try:
        num = int(input("Digite um valor: "))

        if num in numbers:
            print("Valor duplicado.")
        else:
            numbers.append(num)
    except ValueError:
        print("Valor invalido. Tente novamente")

    stop = input("Deseja continuar? [S/n] ")

    if stop.lower() == "n":
        break
    elif stop.lower() != "n":
        stop = "s"

print(f"Lista de valores digitados: {sorted(numbers)}")
