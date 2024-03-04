# Imprime no terminal um cabeçalho de decoração, utilizando o método "f-string"
print(f'{"=" * 8} DESAFIO 027 {"=" * 8}')

# Atribui um input do usuário à variável "nome"
nome = input("Digite o seu nome completo: ")

# Imprime no terminal uma f-string multilinha concatenando com a variável "nome" e retornando o resultado das funções "split()"
print(
    f"""
Nome completo: {nome}
Primeiro nome: {nome.split()[0]}
Ultimo nome: {nome.split()[-1]}"""
)
