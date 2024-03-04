print("======== DESAFIO 070 ========")

total_purchase = 0
products_over_1000 = 0
cheapest_product = ""
cheapest_buy = float("inf")

print("\n~~~~~~~~ LOJINHA DO GUS ~~~~~~~~")
print('[Digite "FINALIZAR" em "Nome do produto" para terminar a operação]')

while True:
    product_name = input("Nome do produto: ").capitalize()
    if product_name.upper() == "FINALIZAR":
        break

    product_value = float(input("Valor do produto: R$"))

    total_purchase += product_value

    if product_value < cheapest_buy:
        cheapest_buy = product_value
        cheapest_product = product_name

    if product_value > 1000:
        products_over_1000 += 1

print(
    f"""
Total da compra: R${total_purchase}
Quantidade de produtos que custam mais de R$1000: {products_over_1000}
Produto mais barato: {cheapest_product}
"""
)
