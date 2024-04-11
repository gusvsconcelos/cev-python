from time import sleep

print(f'{" DESAFIO 089 ":=^29}')

students = list()
student_data = list()

while True:
    student_data.append(input("Nome do aluno: "))
    student_data.append(int(input("Primeira nota do aluno: ")))
    student_data.append(int(input("Segunda nota do aluno: ")))
    student_data.append((student_data[1] + student_data[2]) / 2)
    students.append(student_data[:])
    student_data.clear()

    break_loop: str = input("Desaja continuar? [S/N] ")

    if break_loop in "Nn":
        break

print(f"\n{"="*30}")
print(f"{'BOLETIM DOS ALUNOS':^30}")
print(f"{"="*30}")
for i, student in enumerate(students):
    print(f"NÚM: {i} | NOME: {student[0]:<9} | MÉDIA: {student[3]}")

while True:
    student_number: int = int(input("\nVer as notas de qual aluno? [999 interrompe] "))

    if student_number != 999:
        print(f"\n{"="*30}")
        print(f"{'NOTAS INDIVIDUAIS':^30}")
        print(f"{"="*30}")
        print(
            f"NOME: {students[student_number][0]:<9} | NOTAS: {students[student_number][1]}, {students[student_number][2]}"
        )
    else:
        print("Finalizando...")
        sleep(2)
        print("Volte sempre!")
        break
