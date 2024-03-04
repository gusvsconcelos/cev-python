# Imprime no terminal um cabeçalho de decoração, utilizando o método "f-string"
print(f'{"=" * 8} DESAFIO 034 {"=" * 8}')

# Atribui um input do usuário (número inteiro) à variável "salario"
salario = int(input("Forneça salário do funcionario: "))

# Cria uma condicional que verifica se o salario é maior ou menor que 1250 e aplica uma porcentagem de aumento de acordo
if salario > 1250:
    salario = salario + (salario * 0.10)
    print(
        f"O funcionario recebeu um aumento de 10% no seu salário. Ele irá passar a receber R${salario:.2f} por mês"
    )
else:
    salario = salario + (salario * 0.15)
    print(
        f"O funcionario recebeu um aumento de 15% no seu salário. Ele irá passar a receber R${salario:.2f} por mês"
    )
