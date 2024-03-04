print("======== DESAFIO 071 ========\n")

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("            BANCO CEV            ")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

withdraw = int(input("Digite o valor a ser sacado: "))
money_total = 0
paper_50 = 0
paper_20 = 0
paper_10 = 0
paper_1 = 0

count = 1
while withdraw > 0:
    # 50
    while True:
        if 50 * count <= withdraw:
            paper_50 += 1
            money_total = 50 * count
        else:
            break
        count += 1
    withdraw -= money_total
    money_total = 0
    count = 1

    # 20
    while True:
        if 20 * count <= withdraw:
            paper_20 += 1
            money_total = 20 * count
        else:
            break
        count += 1
    withdraw -= money_total
    money_total = 0
    count = 1

    # 10
    while True:
        if 10 * count <= withdraw:
            paper_10 += 1
            money_total = 10 * count
        else:
            break
        count += 1
    withdraw -= money_total
    money_total = 0
    count = 1

    # 1
    while True:
        if 1 * count <= withdraw:
            paper_1 += 1
            money_total = 1 * count
        else:
            break
        count += 1
    withdraw -= money_total
    money_total = 0
    count = 1

if paper_50 > 0:
    print(f"Total de {paper_50} notas de R$50")
if paper_20 > 0:
    print(f"Total de {paper_20} notas de R$20")
if paper_10 > 0:
    print(f"Total de {paper_10} notas de R$10")
if paper_1 > 0:
    print(f"Total de {paper_1} notas de R$1")

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
