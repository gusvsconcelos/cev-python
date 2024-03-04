import os

messages = []

name = input("Nome: ")

while True:
    os.system("cls")

    if len(messages) > 0:
        for m in messages:
            print(f"\033[33m {m["name"]}\033[m ~ \033[34m{m["text"]}\033[m")      
    print("______________________________")
    text = input("Mensagem: ").capitalize()
    
    if text == "Fim":
        break
    
    messages.append({
        "name": name,
        "text": text
    })
