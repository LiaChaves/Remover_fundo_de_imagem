from rembg import remove
# fornece ao interpretador python recursos de edição de imagem
from PIL import Image
import os

print('Removendo o fundo da imagem...')
pasta_atual = os.getcwd()
arquivos = os.listdir(pasta_atual)

# Filtrar apenas arquivos de imagem (extensões comuns)
extensoes_imagem = [f for f in arquivos if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.jfif', '.webp'))]

imagens = extensoes_imagem[0]  # Pega a primeira imagem encontrada na pasta

img_entrada = imagens
img_saida = imagens.split('.')[0] + '_sem_fundo.png'
input = Image.open(img_entrada)
output = remove(input)
#salvando a imagem
output.save(img_saida)