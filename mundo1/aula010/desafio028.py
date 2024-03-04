# Faz a importação das funções "randint" e "sleep" das bibliotecas "random" e "time"
from random import randint
from time import sleep

# Imprime no terminal um cabeçalho de decoração, utilizando o método "f-string"
print(f'{"=" * 8} DESAFIO 028 {"=" * 8}')

# Um loop que combinado com a biblioteca "time" cria uma simples animação de reticências crescente na variável "message"
for c in range(2):
    message = "O PC está pensando"
    for i in range(4):
        print(f'{message}{"." * i}', end="\r")
        sleep(0.5)

# Atribui um número aleatório entre 0 e 5 à variável "pc_num"
pc_num = randint(0, 5)

# Imprime uma mensagem no terminal
print("\nO PC terminou de pensar. Agora é sua vez!")

# Pede um input (número inteiro) ao usuário e guarda numa variável
user_guess = int(input("Advinhe qual número entre 0 e 5 o PC pensou: "))

# Cria uma condicional que compara o input do resultado com o número gerado aleatorio e imprime no terminal o resultado da comparação
if user_guess == pc_num:
    print("Parabéns, você adivinhou!")
else:
    print(f"Sinto muito, você errou. O PC pensou no número {pc_num}")
