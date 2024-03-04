from random import randint

print("======== DESAFIO 068 ========")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("         PAR OU IMPAR         ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

pc_num = randint(1, 10)

while True:
    user_num = int(input("Digite um valor entre 1 e 10: "))
    user_choice = input("Impar ou Par? [I/P] ")
    even_odd = (user_num + pc_num) % 2

    if user_choice.lower() == "i" and even_odd == 1:
        print("=======================================")
        print(f"Você jogou {user_num} e o PC jogou {pc_num}, DEU IMPAR!")
        print("=======================================")
        print("VOCÊ VENCEU!!!")
        print("Vamos jogar novamente...")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    elif user_choice.lower() == "i" and even_odd == 0:
        print("=======================================")
        print(f"Você jogou {user_num} e o PC jogou {pc_num}, DEU PAR!")
        print("=======================================")
        print("VOCÊ PERDEU!!!")
        break
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    elif user_choice.lower() == "p" and even_odd == 0:
        print("=======================================")
        print(f"Você jogou {user_num} e o PC jogou {pc_num}, DEU PAR!")
        print("=======================================")
        print("VOCÊ VENCEU!!!")
        print("Vamos jogar novamente...")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    elif user_choice.lower() == "p" and even_odd == 1:
        print("=======================================")
        print(f"Você jogou {user_num} e o PC jogou {pc_num}, DEU IMPAR!")
        print("=======================================")
        print("VOCÊ PERDEU!!!")
        break
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
