# Imprime no terminal um cabeçalho de decoração, utilizando o método "f-string"
print(f'{"=" * 8} DESAFIO 022 {"=" * 8}')

# Atribui à variável "nome" uma string com os possíveis espaços excessivos removidos
nome = input("Digite o seu nome completo: ").strip()

# Imprime no terminal uma mensagem concatenada com o método "f-string" e strings multilinha para formatação
print(
    f"""\nSeu nome completo em caixa-alta: {nome.upper()}
Seu nome completo em letras minúsculas: {nome.lower()}
Quantidade de letras presentes no seu nome: {len(nome.replace(' ', ''))}
Quantas letras tem o primeiro nome: {len(nome.split()[0])}"""
)
