# Imprime no terminal um cabeçalho de decoração, utilizando o método "f-string"
print(f'{"=" * 8} DESAFIO 010 {"=" * 8}')

# Atribui o input do usuário (um número real) à variável "real"
real = float(input("\nQuantos reais você tem? R$"))
cota_dolar = 4.93  # Atribui um valor para a cotação do Dolar
cota_euro = 5.37  # Atribui uma valor para a cotação do Euro

# Imprime no terminal uma mensagem concatenando as variáveis anteriores com o método "f-string"
print(
    f"\nVocê possui R${real}. Com esse valor, você pode comprar US${real / cota_dolar:.2f} e €{real / cota_euro:.2f}"
)
