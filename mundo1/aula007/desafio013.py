# Imprime no terminal um cabeçalho de decoração, utilizando o método "f-string"
print(f'{"=" * 8} DESAFIO 013 {"=" * 8}')

# Atribui o input do usuário (um número real) à variável "salario"
salario = float(input("\nForneça o salário do funcionário: "))

# Imprime no terminal uma mensagem concatenando as variáveis anteriores com o método "f-string"
print(
    f"\nO funcionário recebeu um aumento de 15% no salário. Agora ele irá receber ${salario + (salario * 15 / 100):.2f} reais. "
)
