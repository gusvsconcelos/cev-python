# Simplesmente imprime no terminal uma string com um cabeçalho de decoração
print("======== DESAFIO 004 (otimizado) ========")

# Atribui o input do usuário à variável "data"
data = input("\nDigite algo: ")

# Cria uma lista contendo todos os rótulos que serão usados na tabela de verificação de tipagem
info_labels = [
    "É númerico",
    "É alfabeto",
    "É alfanumérico",
    "Contêm apenas maiúsculas",
    "Contêm apenas minúsculas",
    "É imprimível",
    "É decimal",
    "É um identificador",
    "É um espaço",
    "É dígito",
    "É ascii",
    "Está capitalizado",
]

# Cria uma lista contendo todas as funções que serão utilizadas para fazer a verificação de tipagem da variável "data"
info_functions = [
    str.isnumeric,
    str.isalpha,
    str.isalnum,
    str.isupper,
    str.islower,
    str.isprintable,
    str.isdecimal,
    str.isidentifier,
    str.isspace,
    str.isdigit,
    str.isascii,
    str.istitle,
]

# Uma list comprehension é uma construção sintática em Python que permite criar listas de forma concisa. Ela é composta por uma expressão seguida por pelo menos um "for" e zero ou mais "if". A list comprehension executa a expressão para cada item em uma sequência (por exemplo, uma lista, uma string ou um intervalo) e cria uma nova lista com os resultados. Essa list comprehension cria uma nova lista contendo o resultado da verificação de tipagem da variável "data"
info_results = [func(data) for func in info_functions]

# Imprime no terminal o título da tabela de resultados e o tipo primitivo do dado fornecido
print("\nInformações sobre o dado fornecido:\n")
print(f"Tipo de dado: {type(data)}")

# Cria um loop para gerar a tabela de resultados
# A função 'zip()' em Python é usada para combinar elementos de duas ou mais listas (ou outras sequências) em tuplas. Ela cria um iterador que gera tuplas contendo elementos correspondentes das sequências de entrada. O comprimento do resultado é determinado pelo comprimento da sequência mais curta
for label, result in zip(info_labels, info_results):
    print(f"{label}: {result}")
