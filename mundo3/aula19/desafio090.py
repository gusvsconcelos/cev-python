print(f'{" DESAFIO 090 ":=^29}')

student_status = dict()

student_name = input(f"Nome do aluno: ")
student_avarage_grade = float(input(f"Média do aluno: "))

student_status["Nome"] = student_name
student_status["Média"] = student_avarage_grade

if student_avarage_grade >= 7:
    student_status["Situação"] = "Aprovado"
else:
    student_status["Situação"] = "Reprovado"

for k, v in student_status.items():
    print(f"{k}: {v}")
