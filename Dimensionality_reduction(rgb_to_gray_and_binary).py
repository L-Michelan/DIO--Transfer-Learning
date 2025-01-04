def ler_imagem(filepath):
    with open(filepath, 'rb') as f:
        return f.read()

def salvar_imagem(filepath, data):
    with open(filepath, 'wb') as f:
        f.write(data)

def converter_para_cinza(dados, largura, altura):
    nova_imagem = bytearray()
    for i in range(0, len(dados), 3):  # Percorre os bytes R, G e B
        r, g, b = dados[i], dados[i+1], dados[i+2]
        # Calcula a luminância
        cinza = int(0.299 * r + 0.587 * g + 0.114 * b)
        # Adiciona o mesmo valor de cinza para R, G e B
        nova_imagem.extend([cinza, cinza, cinza])
    return nova_imagem

def converter_para_preto_branco(dados, largura, altura, limiar=128):
    nova_imagem = bytearray()
    for i in range(0, len(dados), 3):
        r, g, b = dados[i], dados[i+1], dados[i+2]
        # Converte o tom de cinza para binário (preto ou branco)
        media = (r + g + b) // 3
        valor_binario = 255 if media >= limiar else 0
        nova_imagem.extend([valor_binario, valor_binario, valor_binario])
    return nova_imagem


caminho_imagem = 'Lena.raw'
largura, altura = 850, 850  
# Lê os dados da imagem RGB
dados_rgb = ler_imagem(caminho_imagem)

# Converte para tons de cinza
dados_cinza = converter_para_cinza(dados_rgb, largura, altura)
salvar_imagem('imagem_cinza.rgb', dados_cinza)

# Converte para preto e branco
dados_binarios = converter_para_preto_branco(dados_cinza, largura, altura)
salvar_imagem('imagem_binaria.rgb', dados_binarios)