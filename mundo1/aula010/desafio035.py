# Imprime no terminal um cabeçalho de decoração, utilizando o método "f-string"
print(f'{"=" * 8} DESAFIO 035 {"=" * 8}')

# Cria uma lista vazia
lados_triangulo = []

# Cria um loop que preenche a lista com inputs do usuário
for i in range(3):
    retas = int(input(f"Digite o {i + 1}\u00b0 lado do triângulo: "))
    lados_triangulo.append(retas)

# Atribui para três variáveis os inputs da lista reorganizados em ordem crescente
a, b, c = sorted(lados_triangulo)

# Cria uma condicional que performa o calculo de condição de existência de um triângulo e retorna o resultado
if a + b > c:
    print("É possivel formar um triângulo com os lados fornecidos")
else:
    print("Não é possivel formar um triângulo com os lados fornecidos")
