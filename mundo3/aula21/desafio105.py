""" Analyzing and generating dictionaries """

from statistics import mean


def header():
    """ Print the program header """

    print(f'{" DESAFIO 105 ":=^29}')


def grades(* g, sit=False):
    """
    Analyzes grades and returns a summary including total number of grades, 
    highest grade, lowest grade, average grade, and optionally the overall 
    situation based on the average grade.

    Args:
        *g (float): Grades of students.
        sit (bool, optional): Whether to include the overall situation based on 
            the average grade. Defaults to False.

    Returns:
        dict: A dictionary containing the following keys:
            - 'Total' (int): Total number of grades.
            - 'Maior' (float): Highest grade.
            - 'Menor' (float): Lowest grade.
            - 'Média' (float): Average grade.
            - 'Situação' (str): Overall situation ('BOA', 'RAZOAVEL', or 'RUIM') 
                -> based on the average grade.
                -> it'll only be displayed if sit is True.
    """

    students = {
        'Total': len(g),
        'Maior': max(g),
        'Menor': min(g),
        'Média': mean(g),
        'Situação': 'BOA' if mean(g) > 7 else (
            'RAZOAVEL' if mean(g) >= 6 else 'RUIM'
        )
    }

    if not sit:
        del students['Situação']
        print(students)
    else:
        print(students)


def main():
    """ Initialize program """

    header()
    grades(8, 4, 7, 6, sit=True)


if __name__ == "__main__":
    main()
