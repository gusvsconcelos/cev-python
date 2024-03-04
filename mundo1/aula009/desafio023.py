# Imprime no terminal um cabeçalho de decoração, utilizando o método "f-string"
print(f'{"=" * 8} DESAFIO 023 {"=" * 8}')

# Atribui um número em string á variável "num"
num = input("Forneça um número de 0 a 9999: ")

# Usando strings:
print(
    f"""
Unidade: {num[3:]}
Dezena: {num[2:3]}
Centena: {num[1:2]}
Milhar: {num[:1]}"""
)

# Usando operações matemáticas (preferido para esse exercício):
int_num = int(num)

print(
    f"""
Unidade: {int_num % 10}
Dezena: {(int_num // 10) % 10}
Centena: {(int_num // 100) % 10}
Milhar: {(int_num // 1000) % 10}"""
)

# Usando estrutura de repetição (for):
digitos = []

for d in num:
    digitos.append(int(d))

print(
    f"""
Unidade: {digitos[-1]}
Dezena: {digitos[-2] if len(digitos) > 1 else 0}
Centena: {digitos[-3] if len(digitos) > 2 else 0}
Milhar: {digitos[-4] if len(digitos) > 3 else 0}"""
)
