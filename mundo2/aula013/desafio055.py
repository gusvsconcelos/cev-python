print(f'{"=" * 8} DESAFIO 055 {"=" * 8}')

users_weight = []

for i in range(5):
    users_weight.append(float(input(f"Forneça o peso do {i + 1}ª usuário: ")))

print(users_weight)

max_weight = users_weight[0]
min_weight = users_weight[0]

for i in range(len(users_weight)):
    if users_weight[i] > max_weight:
        max_weight = users_weight[i]
    elif users_weight[i] < min_weight:
        min_weight = users_weight[i]

print(f"A pessoa mais pesada pesa {max_weight}, e a pessoa mais leve pesa {min_weight}")
