# Imprime no terminal um cabeçalho de decoração, utilizando o método "f-string"
print(f'{"=" * 8} DESAFIO 030 {"=" * 8}')

# Atribui um input do usuário (número inteiro) à variável "num"
num = int(input("Forneça um número: "))

# Cria uma condicional que verifica se o número fornecido é par ou impar
if num % 2 == 0:
    print(f"O número {num} é par")
else:
    print(f"O número {num} é impar")
