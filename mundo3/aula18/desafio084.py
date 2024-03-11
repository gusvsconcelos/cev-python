print(f'{" DESAFIO 084 ":=^29}')

users = []

while True:
    name = input("Nome: ")
    weight = int(input("Peso: "))
    users.append([name, weight])
    break_loop = input("Quer continuar? [S/N] ")

    if break_loop in "Nn":
        break

heavier = lighter = users[0][1]

for user in users:
    if user[1] > heavier:
        heavier = user[1]
    elif user[1] < lighter:
        lighter = user[1]

print(f'Número de usúarios cadastrados: {len(users)}')

print(f'O maior peso foi de {heavier}kg. E é o peso de:', end=' ')
for user in users:
    if user[1] == heavier:
        print(user[0], end=' ')

print(f'\nO menor peso foi de {lighter}kg. E é o peso de:', end=' ')
for user in users:
    if user[1] == lighter:
        print(user[0], end=' ')
