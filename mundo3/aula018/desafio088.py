from random import randint
from time import sleep

print(f'{" DESAFIO 088 ":=^29}')

megasena_games: list[int] = list()

number_of_games: int = int(input("Quantos jogos você quer que eu sorteie? "))

for i in range(number_of_games):
    game_row: list[int] = list()
    for j in range(6):
        random_num = randint(1, 60)
        while random_num in game_row:
            random_num = randint(1, 60)
        game_row.append(random_num)
        game_row.sort()
    megasena_games.append(game_row)

for i, row in enumerate(megasena_games):
    print(f"Jogo {i + 1}: {row}")
    sleep(2)
