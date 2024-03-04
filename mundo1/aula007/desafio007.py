# Imprime no terminal um cabeçalho de decoração, utilizando o metodo de concatenação simples
print("=" * 8, " DESAFIO 007 ", "=" * 8)

# Atribui o input do usuário (um número real) à variável "aluno1" e "aluno2"
aluno1 = float(input("\nForneça nota do primeiro aluno: "))
aluno2 = float(input("Forneça a nota do segundo aluno: "))

# Imprime no terminal uma mensagem concatenando as variáveis anteriores com o método "f-string" e com a formatação de string ":.1f"
print(f"\nA média dos alunos é {(aluno1 + aluno2) / 2:.1f}")
