print(f'{" DESAFIO 083 ":=^29}')

num = input("expressão: ")

if num.count("(") == num.count(")"):
    print("Sua expressão está correta")
else:
    print("Sua expressão está errada")
