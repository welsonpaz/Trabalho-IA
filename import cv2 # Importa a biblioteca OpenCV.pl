import cv2  # Importa a biblioteca OpenCV

# Carregar a imagem 'paisagem.jpg' no formato padrão (colorido)
imagem = cv2.imread('C:\Users\Administrator\Pictures\paisagem.jpg')

# Verifica se a imagem foi carregada corretamente
if imagem is None:
    print("Erro ao carregar a imagem. Verifica se o ficheiro 'paisagem.jpg' existe no caminho correto.")
else:
    # Exibe a imagem numa janela chamada 'Exibição de Imagem'
    cv2.imshow('Exibição de Imagem', imagem)

    # Aguarda a pressionar de qualquer tecla. O '0' significa espera indefinida
    cv2.waitKey(0)

    # Fecha todas as janelas abertas pelo OpenCV
    cv2.destroyAllWindows()