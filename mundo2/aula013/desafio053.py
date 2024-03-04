print(f'{"=" * 8} DESAFIO 053 {"=" * 8}')

text = input(f"Digite uma frase qualquer: ").replace(" ", "")
inverted_text = text[::-1]

print(inverted_text)

if text == inverted_text:
    print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo")
