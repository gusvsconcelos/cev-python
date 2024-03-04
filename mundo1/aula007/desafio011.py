# Imprime no terminal um cabeçalho de decoração, utilizando o método "f-string"
print(f'{"=" * 8} DESAFIO 011 {"=" * 8}')

# Atribui o input do usuário (um número inteiro) às variáveis "wall_height" e "wall_width"
wall_height = int(input("\nQual a altura em metros da sua parede? "))
wall_width = int(input("\nQual a largura em metros da sua parede? "))

# Imprime no terminal uma mensagem concatenando as variáveis anteriores com o método "f-string"
print(
    f"\nSua parede tem a dimensão de {wall_height}x{wall_width} e sua área é de {wall_width * wall_height}m². Você irá precisar de {(wall_height * wall_width) / 2} litros de tinta para pintar toda a parede"
)
