# Imprime no terminal um cabeçalho de decoração, utilizando o método "f-string"
print(f'{"=" * 8} DESAFIO 009 {"=" * 8}')

# Atribui o input do usuário (um número inteiro) à variável "num"
num = int(input("\nForneça um número para ver a tabuada: "))

# Imprime no terminal um cabeçalho de decoração, utilizando o método "f-string"
print(f'\n{"-" * 8} TABUADA DO {num} {"-" * 8}')

# Utiliza uma estrutura de repetição que multiplica o número fornecido com todos os números entre 1 e 10
for i in range(1, 11):
    # Utiliza uma estrutura condicional que verifica se o número é menor que 10 e ajusta a formatação a partir disso
    if i < 10:
        print(f"{num} X {i}  = {num * i}")
    else:
        print(f"{num} X {i} = {num * i}")

# Imprime no terminal um cabeçalho de decoração, utilizando o método "f-string" e ajusta o comprimento da linha de acordo com a quantidade de dígitos na variável "num"
print(f'{"-" * (29 + len(str(num)))}')
