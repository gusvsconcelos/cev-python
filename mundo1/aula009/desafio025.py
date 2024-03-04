# Imprime no terminal um cabeçalho de decoração, utilizando o método "f-string"
print(f'{"=" * 8} DESAFIO 025 {"=" * 8}')

# Atribui um input do usuário à variável "nome"
nome = input("Digite o seu nome: ")

# if nome.lower().find('silva') != -1:
#    print('Parabéns, você é um Silva!')
# else:
#    print('Você não é um silva :c')

# Cria uma condicional que verifica se existe "Silva" no nome do usuário e imprime o resultado
if "silva" in nome.lower():
    print("Parabéns, você é um Silva!")
else:
    print("Você não é um silva :c")
