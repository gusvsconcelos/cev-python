from datetime import datetime

print(f'{"=" * 8} DESAFIO 054 {"=" * 8}')

minor = 0
major = 0

for i in range(7):
    birth_year = int(input(f"Ano de nascimento da {i + 1}ª pessoa: "))
    if (datetime.now().year - birth_year) >= 21:
        major += 1
    else:
        minor += 1

print(f"Existem {major} pessoas maiores de idade e {minor} menores de idade")
