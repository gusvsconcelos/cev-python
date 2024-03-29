from typing import Any

print(f'{" DESAFIO 095 ":=^29}')

soccer_team: list[Any] = []
player_data: dict[str, Any] = {}
scores: list[int] = []

while True:
    player_data["Nome"] = input("Nome do jogador: ").capitalize()
    matches = int(input(f'Quantas partidas {player_data["Nome"]} jogou? '))

    for i in range(matches):
        scores.append(int(input(f"Quantos gols na partida {i + 1}? ")))

    player_data["Gols"] = scores.copy()
    player_data["Total"] = sum(scores)
    scores.clear()

    soccer_team.append(player_data.copy())

    break_loop: str = input('Quer continuar? [S/N] ').upper()

    if break_loop == 'N':
        break

print("-=" * 25)
print(f'{"Nª":<4}{"NOME":<20}{"GOLS":<20}{"TOTAL"}')
print("-" * 50)

for i, p in enumerate(soccer_team):
    print(f'{i:<4}{p['Nome']:<18}{str(p['Gols']):<22}{p['Total']}')
print("-" * 50)

while True:
    index = int(input('Mostrar dados de qual jogador? (999 para parar) '))

    while index >= len(soccer_team) and index < 999:
        print(f'ERRO! Não existe jogador com o index {index}!')
        index = int(input('Mostrar dados de qual jogador? (999 para parar) '))

    if index == 999:
        print('-- VOLTE SEMPRE --')
        break
    else:
        print(
            f'-- LEVANTAMENTO DO JOGADOR {soccer_team[index]['Nome'].upper()} --')
        for i in range(len(soccer_team[index]['Gols'])):
            print(f'   No jogo {i + 1} fez {soccer_team[index]['Gols'][i]}')
