# Simplesmente imprime no terminal uma string com um cabeçalho de decoração
print("======== DESAFIO 004 ========")

# Atribui o input do usuário à variável "data"
# Utiliza o 'escape character' "\n" no início para pular uma linha antes da mensagem de input
data = input("\nDigite algo: ")

# Atribui o valor booleano do input do usuário contido na variável "data" a uma nova variável correspondente
numeric = data.isnumeric()
alpha = data.isalpha()
alnum = data.isalnum()
upper = data.isupper()
lower = data.islower()
printable = data.isprintable()
decimal = data.isdecimal()
identifier = data.isidentifier()
space = data.isspace()
digit = data.isdigit()
ascii = data.isascii()
title = data.istitle()

# Imprime no terminal uma mensagem concatenada com as variáveis atribuidas acima utilizando o método ".format()"
# Isso cria uma tabela contendo a verificação do tipo dos dados que o usuário forneceu anteriomente
print("\nInformações sobre os dados fornecidos:\n")
# Utiliza o 'escape character' "\n" no início e no final para pular uma linha antes e depois da mensagem imprimida
print("Tipo de dado:", type(data))
print("É númerico: {}".format(numeric))
print("É alfabeto: {}".format(alpha))
print("É alfanumérico: {}".format(alnum))
print("Contêm apenas maiúsculas: {}".format(upper))
print("Contêm apenas minúsculas: {}".format(lower))
print("É imprimível: {}".format(printable))
print("É decimal: {}".format(decimal))
print("É um identificador: {}".format(identifier))
print("É um espaço: {}".format(space))
print("É dígito: {}".format(digit))
print("É ascii: {}".format(ascii))
print("Está capitalizado: {}".format(title))
