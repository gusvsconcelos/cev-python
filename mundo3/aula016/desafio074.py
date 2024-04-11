from random import randint

print("======== DESAFIO 074 ========")

numbers = (
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
)
greater_num = max(numbers)
lesser_num = min(numbers)

for num in numbers:
    print(num, end=" ")

print(f"\nO menor valor da tupla é {lesser_num} e o maior é {greater_num}")
