# Faz a importação da função "datetime" da biblioteca date
from datetime import date

# Imprime no terminal um cabeçalho de decoração, utilizando o método "f-string"
print(f'{"=" * 8} DESAFIO 032 {"=" * 8}')

# Atribui um input do usuário (número inteiro) à variável "ano"
ano = int(
    input(
        'Forneça um ano para verificar se ele é bissexto. Para verificar o ano atual, digite "0": '
    )
)

# Cria uma condicional que verifica se o ano digitado é zero, se for o caso, irá usar o ano real
if ano == 0:
    ano = date.today().year

# Cria uma condicional que verifica se o ano digitado é bissexto ou não
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print(f"O ano {ano} é bissexto")
else:
    print(f"O ano {ano} não é bissexto")
