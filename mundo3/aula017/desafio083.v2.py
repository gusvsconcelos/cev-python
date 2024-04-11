print(f'{" DESAFIO 083 v2 ":=^29}')

parentheses = []
exp = input("expressão: ")

for element in exp:
    if element == "(":
        parentheses.append(element)
    elif element == ")":
        if len(parentheses) > 0:
            parentheses.pop()
        else:
            parentheses.append(element)
            break

if len(parentheses) == 0:
    print("correto")
else:
    print("errado")
