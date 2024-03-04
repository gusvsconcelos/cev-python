# Faz a importação das funções "randint" e "sleep" das bibliotecas "random" e "time"
from random import randint
from time import sleep

# Imprime no terminal um cabeçalho de decoração, utilizando o método "f-string"
print(f'{"=" * 8} DESAFIO 029 {"=" * 8}')

# Gera um loop infinito até que a condicional encontre um carro que esteja acima de 80km/h
car_found = False

while not car_found:
    message = "Monitorando o trafego"
    for i in range(4):
        print(f'{message}{"." * i}', end="\r")
        sleep(0.5)

    car_vel = randint(45, 120)

    if car_vel > 80:
        print(
            f"Um carro foi flagrado acima do limite permitido de 80km/h ({car_vel}km/h) e recebeu uma multa por excesso de velocidade. O valor da multa é de R${(car_vel - 80) * 7:.2f}"
        )
        car_found = True
    else:
        print("Carro dentro do limite permitido de velocidade")
