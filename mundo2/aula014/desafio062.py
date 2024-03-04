print(f'{"=" * 8} DESAFIO 062 {"=" * 8}')

num = int(input("Digite o primeiro termo: "))
r = int(input("Razão da PA: "))

count = 10
while count > 0:
    print(f"{num}", end=" ")

    num += r
    count -= 1

    if count == 0:
        new_terms = input("\nVocê deseja exibir novos termos? [S/N]: ")
        if new_terms.lower() == "s":
            res = int(input("\nQuantos novos termos você deseja que seja mostrado? "))
            count += res
