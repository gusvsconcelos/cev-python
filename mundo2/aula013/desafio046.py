from time import sleep
import emoji

print(f'{"=" * 8} DESAFIO 046 {"=" * 8}')

for i in range(10, 0, -1):
    print(i)
    sleep(1)
print(emoji.emojize(":fireworks:"))
