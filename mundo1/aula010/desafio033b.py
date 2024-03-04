# Imprime no terminal um cabeçalho de decoração, utilizando o método "f-string"
print(f'{"=" * 8} DESAFIO 033 {"=" * 8}')

# Cria uma lista vazia
numeros = []

# Usa um loop para preencher a lista vazia com os inputs do usuário
for i in range(3):
    num = int(input(f"Forneça o {i + 1}\u00b0 número: "))
    numeros.append(num)

# Atribui o maior e o menor número achados na lista à duas variáveis correspondentes
maior = max(numeros)
menor = min(numeros)

# Imprime no terminal uma mensagem concatenada com o método "f-string"
print(f"O maior número digitado foi {maior} e o menor foi {menor}")
