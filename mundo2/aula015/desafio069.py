print("======== DESAFIO 069 ========")

users_greater_than_18 = 0
number_of_males = 0
women_less_than_20 = 0

while True:
    user_name = input("Qual o seu nome? ")
    user_gender = input("Qual o seu sexo? [M/F] ")
    user_age = int(input("Qual a sua idade? "))

    if user_age >= 18:
        users_greater_than_18 += 1
    if user_gender.upper() == "M":
        number_of_males += 1
    if user_gender.upper() == "F" and user_age < 20:
        women_less_than_20 += 1

    break_loop = input("Deseja continuar? [S/N] ")

    if break_loop.upper() == "N":
        break

print(
    f"""
Usuários com mais de 18 anos: {users_greater_than_18}
Quantidade de homens: {number_of_males}
Mulheres com menos de 20 anos: {women_less_than_20}"""
)
