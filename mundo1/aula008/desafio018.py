# Faz a importação da função "radians", "sin", "cos", "tan" da biblioteca "math"
from math import radians, sin, cos, tan

# Imprime no terminal um cabeçalho de decoração, utilizando o método "f-string"
print(f'{"=" * 8} DESAFIO 018 {"=" * 8}')

# Atribui o input do usuário (um número inteiro) à variável "angulo_graus"
angulo_graus = int(input("\nForneça um ângulo qualquer: "))
# Converte "angulo_graus" para radianos e guarda o valor em uma nova variável
angulos_rad = radians(angulo_graus)

# Imprime no terminal uma mensagem concatenando com as variáveis anteriores e calcula o seno, o cosseno e a tangente do ângulo fornecido
print(
    f"\nO ângulo de {angulo_graus}° possui:\nSeno: {sin(angulos_rad):.2f}\nCosseno: {cos(angulos_rad):.2f}\nTangente: {tan(angulos_rad):.2f}"
)
