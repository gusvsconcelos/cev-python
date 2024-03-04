# Imprime no terminal um cabeçalho de decoração, utilizando o metodo de concatenação simples
print("=" * 8, " DESAFIO 005 ", "=" * 8)

# Atribui o input do usuário (um número inteiro) à variável "num"
num = int(input("\nDigite um número: "))

# Imprime no terminal uma mensagem concatenando a variável anterior usando o método "f-string"
print(f"\nO número sucessor de {num} é {num + 1}, e o antecessor é {num - 1}")
