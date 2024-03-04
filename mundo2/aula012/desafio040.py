print(f'{"=" * 8} DESAFIO 040 {"=" * 8}')

aluno_notas = []

for i in range(2):
    nota = float(input(f"Nota {i + 1}: "))
    aluno_notas.append(nota)

print(aluno_notas)

media = (aluno_notas[0] + aluno_notas[1]) / 2

print(f"Sua média é {media:.2f}")

if media >= 7:
    print(f"Parabéns! Você está aprovado!")
elif 5 <= media <= 6.9:
    print(f"Você está em recuperação!")
else:
    print(f"Você está reprovado!")
