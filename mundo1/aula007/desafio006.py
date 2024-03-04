# Imprime no terminal um cabeçalho de decoração, utilizando o metodo de concatenação simples
print("=" * 8, " DESAFIO 006 ", "=" * 8)

# Atribui o input do usuário (um número inteiro) à variável "num"
num = int(input("\nDigite um número: "))

# Imprime no terminal uma mensagem concatenando as variáveis anteriores com o método "f-string"
print(
    f"\nO dobro de {num} é {num * 2}, o triplo é {num * 3}, e a raiz quadrada é {pow(num, (1/2)):.2f}"
)
