print(f'{"=" * 8} DESAFIO 036 {"=" * 8}')

house = int(input("Valor da casa: R$"))
salary = int(input("Seu salário: R$"))
years = int(input("Informe quantos anos de financiamento: "))
installments = house / (years * 12)

if (salary * 0.30) >= (installments):
    print(
        f"Para pagar uma casa de R${house} em {years} anos, a prestação será de R${installments:.2f}. Emprestimo pode ser CONCEDIDO!"
    )
else:
    print(
        f"Para pagar uma casa de R${house} em {years} anos, a prestação será de R${installments:.2f}. Emprestimo NÃO pode ser CONCEDIDO!"
    )
