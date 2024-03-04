print(f"{'=' * 8} DESAFIO 063 {'=' * 8}")

seq = [0, 1]
i = int(input("Comprimento da sequência: "))

while i > 2:
    seq.append(seq[-1] + seq[-2])
    i -= 1

    if i == 2:
        print(
            " ".join(map(str, seq))
        )  # Map function aplies another function to every item on a iterable (as lists, tuples and sets)
