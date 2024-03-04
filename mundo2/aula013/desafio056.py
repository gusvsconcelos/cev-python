print(f'{"=" * 8} DESAFIO 056 {"=" * 8}')


class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def description(self):
        return f"Nome: {self.name}, Idade: {self.age}, Sexo: {self.gender}"


users = []
total_age = 0
oldest_man_age = 0
women_under_20 = 0

for i in range(4):
    print(f"==== Usuário {i + 1} ====")
    name = input("Nome: ")
    age = int(input("Idade: "))
    total_age += age
    gender = input("Sexo [M/F]: ").upper()
    user = User(name, age, gender)

    users.append(user)

    if gender == "M" and age > oldest_man_age:
        oldest_man_age = age
        oldest_man = name
    if gender == "F" and age > 20:
        women_under_20 += 1

for user in users:
    print(f"\n{user.description()}")

print(f"\nMédia de idade dos usuários: {total_age / 4}")
print(f"Homem mais velho: {oldest_man}")
print(f"Mulheres com menos de 20 anos: {women_under_20}")
