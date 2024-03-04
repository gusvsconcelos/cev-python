from random import randint
from time import sleep


def initial_message():
    print(f'{"=" * 8} DESAFIO 045 {"=" * 8}')

    print(
        f"""
-{"=-" * 4} JOKENPÔ -{"=-" * 4}
[1] PEDRA
[2] PAPEL
[3] TESOURA
-{"=-" * 4} JOKENPÔ -{"=-" * 4}
"""
    )


def get_player_choice():
    return int(input("Qual a sua jogada? "))


def get_pc_choice():
    return randint(1, 3)


def show_jokenpo():
    print("\nJO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PÔ\n")
    sleep(0.3)


def get_results(player_choice, pc_choice):
    jokenpo = {1: "pedra", 2: "papel", 3: "tesoura"}

    if player_choice == pc_choice:
        print(f"EMPATE!!!\nVocê e a máquina jogaram {jokenpo[player_choice]}")
    elif (player_choice, pc_choice) in [(1, 2), (2, 3), (3, 1)]:
        print(f"PERDEU!!!\nA máquina jogou {jokenpo[pc_choice]}")
    else:
        print(f"GANHOU!!!\nA máquina jogou {jokenpo[pc_choice]}")


def main():
    initial_message()
    player_choice = get_player_choice()
    pc_choice = get_pc_choice()
    show_jokenpo()
    get_results(player_choice, pc_choice)


if __name__ == "__main__":
    main()
