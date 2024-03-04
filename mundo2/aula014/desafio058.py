from random import randint
from time import sleep

print(f'{"=" * 8} DESAFIO 058 {"=" * 8}')

pc_choice = randint(0, 10)

message = "O PC está pensando"
for i in range(3):
    message += "."
    print(message, end="\r")
    sleep(1)
print("O PC pensou num número. Agora é sua vez de tentar advinhar.")

player_choice = int(input("Seu palpite: "))

error_count = 1
while player_choice != pc_choice:
    try:
        player_choice = int(input("ERRADO. Tente novamente: "))
    except ValueError:
        print("Valor digitado inválido.")
    error_count += 1

print(f"Parabéns, você acertou. A quantidade de tentativas foram: {error_count}")
