""" Player Info """


def header():
    """ Print the program header """

    print(f'{" DESAFIO 103 ":=^29}')


def player_info(name='<desconhecido>', goals=0):
    """
    Prints the player's name and the number of goals scored.

    Args:
        player_name (str, optional): The name of the player.
            Defaults to <desconhecido> (unknown).
        goals (int, optional): The number of goals scored.
            Defaults to 0.

    Returns:
        None
    """

    print(f'O jogador {name} marcou {goals} gols no campeonato.')


def init_player():
    """
    Receive the input of the player's name and the number of goals scored, and
    then return them as parameters to the player_info() function.

    If one or both of the input variables are empty or invalid, the
    player_info() function will use its defaults.
    """

    name = input('Nome do jogador: ')
    goals = input('Gols marcados: ')

    if name and goals.isnumeric():
        return player_info(name, goals=int(goals))
    if not name and goals.isnumeric():
        return player_info(goals=int(goals))
    if name and not goals.isnumeric():
        return player_info(name=name)

    return player_info()


def main():
    """ Initialize program """

    header()
    init_player()


if __name__ == "__main__":
    main()
