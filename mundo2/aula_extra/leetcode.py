s = "loveleetcode"

# Cria um dicionário vazio
counts = {}

# Itera sobre a string e preenche o dicionário com cada letra da string como chave, recebendo a contagem de repetições dessa letra como valor
for char in s:
    # Verifica com o método get() se a letra já existe no dicionário, e se não exisir ela será inicializada com o valor 0, se existir, será somado 1 ao valor a cada iteração
    counts[char] = counts.get(char, 0) + 1

# Itera por uma segunda vez sobre a string, dessa vez sobre os seus indices ao invés de seus caracteres
for i in range(len(s)):
    # Verifica se o caractere dentro do dicionário, referente ao indice atual (s[i]), possui um valor de contagem igual a 1, e retorna o indice desse caractere caso verdadeiro e encerra o loop
    if counts[s[i]] == 1:
        print(i)
        break

# Se o loop finalizar sem encontrar nenhum caractere que não se repita na string, retorna -1.
else:
    print(-1)
