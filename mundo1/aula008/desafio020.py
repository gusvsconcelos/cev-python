# Faz a importação da função "shuffle" da biblioteca "random"
from random import shuffle

# Imprime no terminal um cabeçalho de decoração, utilizando o método "f-string"
print(f'{"=" * 8} DESAFIO 020 {"=" * 8}')

# Cria uma lista vazia
lista_alunos = []

# Utiliza de uma estrutura de repetição para preencher a lista com nomes de alunos
for i in range(4):
    nome_aluno = input("Nome do aluno: ")
    lista_alunos.append(nome_aluno)

# Embaralha a lista de alunos com a função "shuffle"
shuffle(lista_alunos)

# Imprime no terminal um cabeçalho de decoração, utilizando o método "f-string"
print(f'\n{"-" * 4} ORDEM DE APRESENTAÇÃO DOS ALUNOS {"-" * 4}')

# Utiliza uma estrutura de repetição com a função "enumerate" que percorre pela quantidade de itens na lista para criar uma tupla com um contador e um nome de aluno atribuído
for num, aluno in enumerate(lista_alunos, 1):
    print(f"{num:02d}: {aluno}")
