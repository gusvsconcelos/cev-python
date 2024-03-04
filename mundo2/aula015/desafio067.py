print("======== DESAFIO 067 ========")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("           TABUADA           ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

i = 1
while True:
    num = int(input("Digite um número: "))

    if num < 0:
        break

    while i <= 10:
        if i < 10:
            print(f"{num} x {i}  =  {num * i}")
        else:
            print(f"{num} x {i} =  {num * i}")
        i += 1
    print("===========================")

    i = 1
