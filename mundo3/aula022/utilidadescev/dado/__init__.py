""" Input Data Analysis """


def money(prompt):
    """
    Takes user input as a string and converts it to a float representing
    a monetary value.
    """

    i = input(prompt)

    while not i.isnumeric():
        if ',' in i:
            i = i.replace(',', '.')
            break
        if '.' in i:
            break

        print(f'\033[91m {
              "Insira um valor válido (inteiros ou de número flutuante)"
              }\033[00m')

        i = input(prompt)

    i = float(i)

    return i
