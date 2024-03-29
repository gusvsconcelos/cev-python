from typing import Any

print(f'{" DESAFIO 094 ":=^29}')

users: list[Any] = []
person: dict[Any, Any] = {}

while True:
    person["Nome"] = input("Nome: ").capitalize()
    person["Sexo"] = input("Sexo: [M/F] ").upper()

    while person["Sexo"] != "M" and person["Sexo"] != "F":
        print('Por favor, responda apenas com "M" ou "F"')
        person["Sexo"] = input("Sexo: [M/F] ").upper()

    person["Idade"] = int(input("Idade: "))

    users.append(person.copy())

    break_point = input("Quer continuar? [S/N] ").upper()

    while break_point != "S" and break_point != "N":
        print('Por favor, responda apenas com "S" ou "N"')
        break_point = input("Quer continuar? [S/N] ").upper()

    if break_point == "N":
        break

print("-=" * 25)
print(f"A) Ao todo temos {len(users)} pessoas cadastradas.")

age_total = 0

for u in users:
    age_total += u["Idade"]

age_avarage = age_total / len(users)

print(f"B) A média de idade é de {age_avarage:.1f} anos.")

print("C) As mulheres cadastradas foram", end=" ")
for u in users:
    if u["Sexo"].lower() == "f":
        print(u["Nome"], end=" ")

print("\nD) Lista de pessoas que estão acima da média:")
for u in users:
    if u["Idade"] > age_avarage:
        print(f'   NOME: {u["Nome"]}; SEXO: {u["Sexo"]}; IDADE: {u["Idade"]};')

print("<< ENCERRADO >>")
