print("======== DESAFIO 077 ========")

words = (
    "aprender",
    "python",
    "gustavo",
    "computador",
    "programar",
    "academia",
    "felicidade",
    "amizade",
    "viagem",
    "musica",
    "videogame",
)

for i in range(len(words)):
    print(f"\nA palavra {words[i].upper()} possui as vogais:", end=" ")
    for c in range(len(words[i])):
        if words[i][c] in "aeiou":
            print(words[i][c], end=" ")
