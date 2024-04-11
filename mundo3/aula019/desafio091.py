from operator import itemgetter
from random import randint
from time import sleep

print(f'{" DESAFIO 091 ":=^29}')

dice_players: dict[str, int] = {
    "Player 1": randint(1, 6),
    "Player 2": randint(1, 6),
    "Player 3": randint(1, 6),
    "Player 4": randint(1, 6),
}

print("Sorteando...", end="\r")
sleep(2)
print("Valores sorteados:")

for player, dice in dice_players.items():
    print(f"{player}: {dice}")
    sleep(1)

# SORTED() METHOD WITH ITEMGETTER
ranking: list[tuple[str, int]] = sorted(
    dice_players.items(), key=itemgetter(1), reverse=True
)

print(f'\n{" RANKING DE JOGADORES ":=^26}')
for i, player in enumerate(ranking):
    print(f"{i + 1}ª {player[0]}: {player[1]}")
    sleep(1)


# USING THE SORTED() METHOD
# for player in sorted(dice_players, key=dice_players.get, reverse=True):
#     print(player, dice_players[player])


# MANUAL SORTING
# dice_items: list[tuple[str, int]] = list(dice_players.items())

# for i in range(len(dice_items)):
#     min_index: int = i
#     for j in range(i + 1, len(dice_items)):
#         if dice_items[j][1] < dice_items[min_index][1]:
#             min_index = j
#     dice_items[i], dice_items[min_index] = dice_items[min_index], dice_items[i]

# dice_game_sorted: dict[str, int] = dict(dice_items)

# print(f'\n{" RANKING DE JOGADORES ":=^26}')

# ranking: int = 1
# for player, dice in dice_game_sorted.items():
#     print(f"{ranking}ª {player}: {dice}")
#     ranking += 1
