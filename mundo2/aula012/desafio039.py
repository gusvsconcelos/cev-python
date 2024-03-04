from datetime import datetime

print(f'{"=" * 8} DESAFIO 039 {"=" * 8}')


class Birth:
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

user_birth = Birth(name, birth_day, birth_month, birth_year)

print(user_birth.description())

age = datetime.now().year - user_birth.year

if age >= 18:
    answer = input("Você já realizou seu alistamento militar? (S/n): ")
    if answer.lower != "s" and answer != "n":
        answer = "s"
        print("Parabéns por cumprir com seu dever civil!")
    elif answer.lower == "s":
        print("Parabéns por cumprir com seu dever civil!")
    else:
        if age == 18:
            print("Você tem 18 anos, é hora de realizar o alistamento militar!")
        elif age > 18:
            print(
                f"já se passaram {age - 18} anos desde que você completou 18. Não perca mais tempo e faça seu alistamento militar na junta mais próxima!"
            )
else:
    print(f"Ainda faltam {18 - age} para você se alistar ao Exército.")
