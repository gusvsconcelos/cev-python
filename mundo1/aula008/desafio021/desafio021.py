# Faz a importação da função "playsound" da biblioteca "playsound"
from playsound import playsound

# Faz a importação da biblioteca "os"
import os

# Atribui à variável "musica_dir" a caminho atual do arquivo usando a função "path.dirname()" e "path.realpath(__file__)"
musica_dir = os.path.dirname(os.path.realpath(__file__))

# Atribui à variável "musica" o caminho atual o arquivo concatenado com o nome do arquivo a ser usado
musica = os.path.join(musica_dir, "musica.mp3")

# Executa a música guardada na variável "musica"
playsound(musica)
