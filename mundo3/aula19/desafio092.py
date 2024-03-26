print(f"{' DESAFIO 092 ':=^29}")

worker = dict()

worker['Nome'] = input('Nome: ')
worker['Ano de nascimento'] = int(input('Ano de nascimento: '))
worker['Carteira de Trabalho'] = int(input('Carteira de Trabalho [0 não tem]: '))

if worker['Carteira de Trabalho'] != 0:
    worker['Ano de contratação'] = int(input('Ano de contratação: '))
    worker['Salário'] = float(input('Salário: R$'))
    worker['Aposentadoria'] = (worker['Ano de contratação'] - worker['Ano de nascimento']) + 35

print('=' * 29)
for label, data in worker.items():
    print(f'{label}: {data}')

