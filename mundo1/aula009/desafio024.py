# Imprime no terminal um cabeçalho de decoração, utilizando o método "f-string"
print(f'{"=" * 8} DESAFIO 024 {"=" * 8}')

# Atribui um input do usuário à variável "cidade"
cidade = input("Forneça o nome de uma cidade: ")

# Cria uma condicional que verifica se a cidade começa com a palavra "santo" ou "são" e imprime o resultado
if cidade.lower().find("santo") == 0 or cidade.lower().find("são") == 0:
    print("A cidade é de Deus")
else:
    print("A cidade não é católica")
