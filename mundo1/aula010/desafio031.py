# Imprime no terminal um cabeçalho de decoração, utilizando o método "f-string"
print(f'{"=" * 8} DESAFIO 031 {"=" * 8}')

# Atribui um input do usuário (número inteiro) à variável "distancia"
distancia = int(input("Informe a distancia da viagem em Km: "))

# Cria uma condicional que verifica se a distancia fornecida é maior ou menor que 200km/h e gera o preço baseado no resultado
if distancia <= 200:
    print(f"O preço da passagem é {distancia * 0.5}")
else:
    print(f"O preço da passagem é {distancia * 0.45}")

# Usando if simplificado:
# preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
# print(preco)
