# Imprime no terminal um cabeçalho de decoração, utilizando o metodo de concatenação simples
print("=" * 8, " DESAFIO 008 ", "=" * 8)

# Atribui o input do usuário (um número inteiro) à variável distMetro
dist_metro = int(input("\nForneça uma distância em metro: "))

# Imprime no terminal uma mensagem concatenando as variáveis anteriores com o método "f-string"
print(
    f"\nDistância em quilômetro: {dist_metro / 1000}km\nDiatância em hectômetro: {dist_metro / 100}hm\nDistância em decâmetro: {dist_metro / 10}dam\nDistância em metro: {dist_metro}m\nDistância em decímetro: {dist_metro * 10}dm\nDistância em centímetro: {dist_metro * 100}cm\nDistância em milímetro: {dist_metro * 1000}mm"
)
