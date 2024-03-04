# Imprime no terminal um cabeçalho de decoração, utilizando o método "f-string"
print(f'{"=" * 8} DESAFIO 033 {"=" * 8}')

# Cria uma lista vazia chamada 'numeros'
numeros = []

# Este loop vai rodar 3 vezes
for i in range(3):
    # Solicita ao usuário para inserir um número
    # O número é convertido para um inteiro e armazenado na variável 'num'
    num = int(input(f"Forneça o {i + 1}\u00b0 número: "))
    # O número é adicionado à lista 'numeros'
    numeros.append(num)

# Inicializa as variáveis 'maior' e 'menor' com o primeiro número da lista
maior = numeros[0]
menor = numeros[0]

# Este loop percorre todos os números na lista 'numeros'
for i in range(len(numeros)):
    # Se o número atual for maior que o valor armazenado em 'maior', atualiza 'maior'
    if numeros[i] > maior:
        maior = numeros[i]
    # Se o número atual for menor que o valor armazenado em 'menor', atualiza 'menor'
    elif numeros[i] < menor:
        menor = numeros[i]

# Imprime o maior e o menor número digitado
print(f"O maior número digitado foi {maior} e o menor foi {menor}")
