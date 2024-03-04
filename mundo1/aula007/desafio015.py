# Imprime no terminal um cabeçalho de decoração, utilizando o método "f-string"
print(f'{"=" * 8} DESAFIO 015 {"=" * 8}')

# Atribui o input do usuário (um número inteiro e um número real) às variáveis "dias_aluguel" e "km_rodados"
dias_aluguel = int(input("\nQuantos dias alugados? "))
km_rodados = float(input("Quantos Km rodados? "))

# Imprime no terminal uma mensagem concatenando as variáveis anteriores com o método "f-string"
print(f"\nO total a pahar é de R${dias_aluguel * 60 + 0.15 * km_rodados:.2f}")
