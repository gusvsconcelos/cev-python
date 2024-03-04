# Simplesmente imprime no terminal uma string com um cabeçalho de decoração
print("======== DESAFIO 003 ========")

# Atribui o input do usuário (um número inteiro) à variável "num1"
num1 = int(input("Primeiro número: "))
print(type(num1))  # Imprime no terminal o tipo de dado contido na variável "num1"

# Atribui o input do usuário (um número inteiro) à variável "num2"
num2 = int(input("Segundo número: "))
print(type(num2))  # Imprime no terminal o tipo de dado contido na variável "num2"

# Atribui à variável "soma" a soma das duas variáveis de número inteiro incializadas anteriomente
soma = num1 + num2

# Imprime no terminal uma mensagem concatenando as variáveis anteriores com o método ".format()"
print("A soma entre {} e {} vale {}".format(num1, num2, soma))
