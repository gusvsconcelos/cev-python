# Imprime no terminal um cabeçalho de decoração, utilizando o método "f-string"
print(f'{"=" * 8} DESAFIO 014 {"=" * 8}')

# Atribui o input do usuário (um número real) à variável "temp_celsius"
temp_celsius = float(input("\nInforme a temperatura em °C: "))

# Imprime no terminal uma mensagem concatenando as variáveis anteriores com o método "f-string"
print(f"\nA temperatura de {temp_celsius}°C corresponde a {temp_celsius * 1.8 + 32}°F")
