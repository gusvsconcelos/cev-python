print("======== DESAFIO 071 v2 ========\n")

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("            BANCO CEV            ")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

withdraw = int(input("Digite o valor a ser sacado: "))
total = withdraw
money_bill = 50
bill_total = 0

while True:
    if total >= money_bill:
        bill_total += 1
        total -= money_bill
    else:
        if bill_total > 0:
            print(f"Total de {bill_total} notas de R${money_bill}")

        if money_bill == 50:
            money_bill = 20
        elif money_bill == 20:
            money_bill = 10
        elif money_bill == 10:
            money_bill = 1

        bill_total = 0

        if total == 0:
            break
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
