"""
Script para padronizar imagens de pandas.
- Redimensiona para 224x224 pixels
- Centraliza em fundo preto
- Renomeia sequencialmente
"""

import os
from PIL import Image

def padronizar_imagem(pasta_origem, pasta_destino, tamanho=(224, 224)):

    """
    Redimensiona e renomeia imagens mantendo proporção e fundo preto.

    Args:
        pasta_origem (str): Diretório com as imagens originais.
        pasta_destino (str): Diretório onde as imagens padronizadas serão salvas.
        tamanho (tuple): Dimensão final (largura, altura), padrão (224, 224).

    Returns:
        None. As imagens são salvas no diretório destino.
    """
    print(f"Padronizando imagens de '{pasta_origem}' para '{pasta_destino}' com tamanho {tamanho}...")

    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    total_processadas = 0
    total_erros = 0

    for i, arquivo in enumerate(sorted(os.listdir(pasta_origem))):
        caminho_arquivo = os.path.join(pasta_origem, arquivo)
        if os.path.isfile(caminho_arquivo):
            try:
                img = Image.open(caminho_arquivo).convert('RGB')
                img.thumbnail(tamanho, Image.Resampling.LANCZOS)
                fundo = Image.new('RGB', tamanho, (0, 0, 0))
                posicao_x = (tamanho[0] - img.width) // 2
                posicao_y = (tamanho[1] - img.height) // 2
                fundo.paste(img, (posicao_x, posicao_y))
                caminho_imagem_padronizada = f"img_{i+1:03d}.jpg"
                caminho_saida = os.path.join(pasta_destino, caminho_imagem_padronizada)
                fundo.save(caminho_saida, "JPEG", quality=95)

                total_processadas += 1

            except ImportError as e:
                print(f" Erro ao processar a imagem '{arquivo}': {e}")
                total_erros += 1

    print(f"Imagens processadas com sucesso: {total_processadas}")
    print(f"Imagens com erro: {total_erros}")
