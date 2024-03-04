# Faz a importação da váriavel "re" que permite o uso de expressões regulares
import re

# Imprime no terminal um cabeçalho de decoração, utilizando o método "f-string"
print(f'{"=" * 8} DESAFIO 026 {"=" * 8}')

# Atribui à variável "frase" uma string com os possíveis espaços excessivos removidos
frase = input("Forneça uma frase: ").strip()

# Imprime no terminal uma f-string multilinha concatenando com a variável "frase" e retornando o resultado das funções "find()"
print(
    f"""
A letra "A" aparece {frase.upper().count('A')} vezes.
A letra "A" aparece pela primeira vez na posição {frase.upper().find('A') + 1}.
A letra "A" aparece pela a ultima vez na posição {frase.upper().rfind('A') + 1}."""
)

# Usando Expressões Regulares para garantir que todas as letras "A" serão contadas mesmo que estejam acentuadas.
# Neste caso específico, como a expressão regular contém apenas caracteres alfanuméricos e não inclui barras invertidas \, o uso do prefixo r não afeta o resultado final. Então, você poderia escrever a expressão regular sem o r, e o código funcionaria da mesma forma.
print(
    f"""
A letra "A" aparece {len(re.findall(r'[aAáÁàÀãÃâÂ]', frase))} vezes.
A letra "A" aparece pela primeira vez na posição {re.search(r'[aAáÁàÀãÃâÂ]', frase).start() + 1}.
A letra "A" aparece pela a ultima vez na posição {re.search(r'[aAáÁàÀãÃâÂ](?!.*[aAáÁàÀãÃâÂ])',frase).start() + 1}."""
)
