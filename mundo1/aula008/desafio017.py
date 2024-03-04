# Faz a importação da função "hypot" da biblioteca "math"
from math import hypot

# Imprime no terminal um cabeçalho de decoração, utilizando o método "f-string"
print(f'{"=" * 8} DESAFIO 017 {"=" * 8}')

# Atribui o input do usuário (um número inteiro) às variáveis "cat_oposto" e "cat_adj"
cat_oposto = int(input(f"\nForneça o valor do cateto oposto: "))
cat_adj = int(input(f"\nForneça o valor do cateto adjacente: "))

# Imprime no terminal uma mensagem concatenando com as variáveis anteriores. Utilizando a função "hypot" para calcular a hipotenusa
print(
    f"\nUm triângulo retângulo com os catetos {cat_oposto} e {cat_adj} possui uma hipotenusa igual a {hypot(cat_oposto, cat_adj):.1f}"
)
