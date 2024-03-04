# Faz a importação da função "choice" da biblioteca "random"
from random import choice

# Imprime no terminal um cabeçalho de decoração, utilizando o método "f-string"
print(f'{"=" * 8} DESAFIO 019 {"=" * 8}')

# Cria uma lista vazia
alunos = []

# Utiliza de uma estrutura de repetição para preencher a lista com nomes de alunos
for i in range(4):
    nome_aluno = input("Nome do aluno: ")
    alunos.append(nome_aluno)

# Imprime no terminal uma mensagem concatenada com o método "f-string" e mostra o resultado da função "choice"
print(f"\nO aluno sorteado foi: {choice(alunos)}")
