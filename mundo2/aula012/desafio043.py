print(f'{"=" * 8} DESAFIO 043 {"=" * 8}')

weight = float(input("Seu peso (em quilogramas): "))
height = float(input("Sua altura (em metros): "))
imc = weight / height**2

if imc < 18.5:
    print(f"Seu IMC é {imc:.2f}. Você está abaixo do peso.")
elif 18.5 <= imc < 25:
    print(f"Seu IMC é {imc:.2f}. Você está com o peso ideal.")
elif 25 <= imc < 30:
    print(f"Seu IMC é {imc:.2f}. Você está com sobrepeso.")
elif 30 <= imc < 40:
    print(f"Seu IMC é {imc:.2f}. Você está com obesidade.")
else:
    print(f"Seu IMC é {imc:.2f}. Você está com obesidade mórbida.")
