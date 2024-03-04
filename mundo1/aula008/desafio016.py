# Faz a importação da função "trunc" da biblioteca "math"
from math import trunc

# Imprime no terminal um cabeçalho de decoração, utilizando o método "f-string"
print(f'{"=" * 8} DESAFIO 016 {"=" * 8}')

# Atribui o input do usuário (um número real) à variável "num"
num = float(input("\nDigite um número: "))

# Imprime no terminal uma mensagem concatenando com a variável anterior. Utilizando a função "trunc" para cortar os decimais do número real e mostrar ele como inteiro
print(f"\nO número {num} tem a parte inteira {trunc(num)}")
