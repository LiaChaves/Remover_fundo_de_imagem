# 🪄 Background Remover com Python & IA

Script em Python que identifica automaticamente uma imagem no diretório e remove o seu fundo utilizando inteligência artificial através da biblioteca `rembg`.

## 🚀 Como Usar

### 1. Pré-requisitos
Certifique-se de ter o Python 3.8+ instalado.

### 2. Instalação das dependências
Clone o repositório e instale as bibliotecas necessárias:

```bash```
pip install -r requirements.txt

### 3. Esse script automatiza a remoção de fundo da primeira imagem encontrada na mesma pasta em que ele é executado:

Importação das Bibliotecas:

    from rembg import remove: Importa o motor de Inteligência Artificial (baseado na rede neural U²-Net). É ele quem detecta o que é pessoa/objeto (primeiro plano) e apaga o restante.

    from PIL import Image: A biblioteca Pillow é o padrão do Python para abrir, manipular e salvar arquivos de imagem na memória.

    import os: Permite que o Python interaja com o sistema operacional do seu computador (ler pastas, listar arquivos).

Leitura da Pasta e Filtro:

    os.getcwd() e os.listdir(): Descobrem em qual pasta o script está e listam tudo o que existe lá dentro.

    extensoes_imagem = [...]: Cria uma lista apenas com arquivos cujas extensões terminem em formatos válidos de imagem (.png, .jpg, .webp, etc.). O .lower() garante que funcione mesmo se o arquivo estiver em maiúsculo (ex: .JPG).

Seleção e Nomes:

    imagens = extensoes_imagem[0]: Pega a primeira imagem da lista.

    img_saida = ...: Define o nome do novo arquivo, adicionando o sufixo _sem_fundo.png. O formato precisa ser .png para suportar o canal alfa (fundo transparente).

Processamento com IA:

    Image.open(img_entrada): Carrega a imagem na memória.

    output = remove(...): A IA analisa os pixels e remove o fundo.

    output.save(img_saida): Salva o arquivo final no disco.