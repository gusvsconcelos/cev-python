print("======== DESAFIO 073 ========")

brasileirao_serie_a = (
    "Palmeiras",
    "Grêmio",
    "Atlético-MG",
    "Flamengo",
    "Botafogo",
    "Bragantino",
    "Fluminense",
    "Athletico-PR",
    "Internacional",
    "Fortaleza",
    "São Paulo",
    "Cuiabá",
    "Corinthians",
    "Cruzeiro",
    "Vasco",
    "Bahia",
    "Santos",
    "Goiás",
    "Coritiba",
    "América-MG",
    "Chapecoense",
)

print("\n=============================")
print("     TABELA DO CAMPEONATO    ")
print("=============================")

for pos, time in enumerate(brasileirao_serie_a):
    if pos < 9:
        print(f"0{pos + 1} - {time}")
    else:
        print(f"{pos + 1} - {time}")


print("\n=============================")
print("       G5 DO CAMPEONATO      ")
print("=============================")

for pos, time in enumerate(brasileirao_serie_a[0:6]):
    if pos < 9:
        print(f"0{pos + 1} - {time}")
    else:
        print(f"{pos + 1} - {time}")

print("\n=============================")
print("       Z5 DO CAMPEONATO      ")
print("=============================")

for pos, time in enumerate(brasileirao_serie_a[16:]):
    print(f"{pos + 17} - {time}")

print("\n=============================")
print("  TABELA EM ORDEM ALFABETICA ")
print("=============================")

for pos, time in enumerate(sorted(brasileirao_serie_a)):
    if pos < 9:
        print(f"0{pos + 1} - {time}")
    else:
        print(f"{pos + 1} - {time}")

print("\n=============================")
print("    POSIÇÃO DA CHAPECOENSE   ")
print("=============================")
index_chape = brasileirao_serie_a.index("Chapecoense")

print(f"Chape se encontra na posição {index_chape + 1} da tabela")
