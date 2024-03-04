# Utilização de cores no Python

print(f'\033[33m{"-=-" * 10}\033[m')
print("\033[34m       CORES EM PYTHON\033[m")
print(f'\033[33m{"-=-" * 10}\033[m')

nome = input("\033[37mDigite seu nome: \033[m")

# Dicionário que atribui os códigos de cores a novas palavras
cores = {
    "limpa": "\033[m",
    "branco": "\033[30m",
    "vermelho": "\033[31m",
    "verde": "\033[32m",
    "amarelo": "\033[33m",
    "azul": "\033[34m",
    "lilas": "\033[35m",
    "ciano": "\033[36m",
    "cinza": "\033[37m",
    "pretoebranco": "\033[7;30m",
}

print(
    f'{cores["azul"]}Olá! Muito prazer em te conhecer{cores["limpa"]}, {cores["amarelo"]}{nome}!!!{cores["limpa"]}'
)
