# Imprime no terminal um cabeçalho de decoração, utilizando o método "f-string"
print(f'{"=" * 8} DESAFIO 012 {"=" * 8}')

# Atribui o input do usuário (um número real) à variável "produto_preco"
produto_preco = float(input("\nForneça o preço do produto: "))

# Imprime no terminal uma mensagem concatenando as variáveis anteriores com o método "f-string"
print(
    f"\nO novo preço do produto com o desconto de 5% aplicado é: ${produto_preco - (produto_preco * 5 / 100):.2f}"
)
