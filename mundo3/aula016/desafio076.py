print("======== DESAFIO 076 ========")

products = (
    "Pão (Unidade)",
    0.50,
    "Bolacha Recheada",
    2.00,
    "Coca-Cola (2l)",
    4.00,
    "Bolo de Fubá",
    6.00,
    "Queijo Mussarela (300g)",
    8.30,
    "Presunto (300g)",
    9.50,
    "Bridadeiro (50 Unidades)",
    12.00,
)

print(f'{"-" * 44}')
print(f"{'TABELA DE PREÇOS':^44}")
print(f'{"-" * 44}')
for i in range(0, len(products), 2):
    try:
        print(f"{products[i]:.<36}R$ {products[i + 1]:.2f}")
    except IndexError:
        break
print(f'{"-" * 44}')
