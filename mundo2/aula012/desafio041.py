from datetime import datetime

print(f'{"=" * 8} DESAFIO 041 {"=" * 8} ')


class Atleta:
    def __init__(self, name, day, month, year):
        self.name = name
        self.day = day
        self.month = month
        self.year = year

    def description(self):
        return f"{self.name}, {self.day}/{self.month}/{self.year}"


name = input("Nome: ")
birth_day = int(input("Dia do nascimento: "))
birth_month = int(input("Mês do nascimento: "))
birth_year = int(input("Ano do nascimento: "))

user_birth = Atleta(name, birth_day, birth_month, birth_year)

print(user_birth.description())

age = datetime.now().year - user_birth.year

if age <= 9:
    print("Mirim")
elif 9 < age <= 14:
    print("Infantil")
elif 14 < age <= 19:
    print("Júnior")
elif 19 < age <= 25:
    print("Sênior")
else:
    print("Master")
