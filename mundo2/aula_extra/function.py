def my_function(value1, value2):
    return value1 + value2


while True:
    value1 = int(input("Digite o primeiro valor: "))
    value2 = int(input("Digite o segundo valor: "))

    if value1 == 0 and value2 == 0:
        break

    answer = my_function(value1, value2)

    print(f"Resultado: {value1} + {value2} = {answer}")
