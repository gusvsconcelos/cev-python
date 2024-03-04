print(f'{"=" * 8} DESAFIO 044 {"=" * 8}')

total_price = float(input("Forneça o preço total das suas compras: R$"))

print(
    f"""
PREÇO TOTAL: R${total_price:.2f}
-{"=-" * 8} FORMA DE PAGAMENTO {"=-" * 8}
• À VISTA DINHEIRO/CHEQUE  (10% DE DESCONTO)   [1]
• À VISTA NO CARTÃO        (5% DE DESCONTO)    [2]
• EM ATÉ 2X NO CARTÃO      (PREÇO FORMAL)      [3]
• 3X OU MAIS NO CARTÃO     (20% DE JUROS)      [4]
-{"=-" * 26}
"""
)

answer = int(input("Escolha a forma de pagamento: "))

if answer == 1:
    total_price *= 0.90
    print(
        f"Você efetuou o pagamento de R${total_price:.2f} (10% de desconto). Obrigado e volte sempre!"
    )
elif answer == 2:
    total_price *= 0.95
    print(
        f"Você efetuou o pagamento de R${total_price:.2f} (5% de desconto). Obrigado e volte sempre!"
    )
elif answer == 3:
    print(
        f"Você efetuou o pagamento da primeira de duas parcelas (R${total_price / 2}). Obrigado e volte sempre!"
    )
elif answer == 4:
    total_price *= 1.60
    print(total_price)
