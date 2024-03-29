from typing import Any

print(f'{" DESAFIO 093 ":=^29}')

player_data: dict[str, Any] = {}
scores = []
player_data["Nome"] = input("Nome do jogador: ")

matches = int(input(f'Quantas partidas {player_data["Nome"]} jogou? '))

for i in range(matches):
    scores.append(int(input(f"Quantos gols na partida {i + 1}? ")))

player_data["Gols"] = scores
player_data["Total"] = sum(scores)

print("-=" * 25)

for k, v in player_data.items():
    print(f"{k}: {v}")

print("-=" * 25)
print(f'O jogador {player_data["Nome"]} jogou {matches} partidas.')

for i in range(matches):
    print(f' => Na partida {i + 1}, fez {player_data["Gols"][i]} gols.')
