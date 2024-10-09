import cv2
 

# Carrega a imagem colorida
img_colorida = cv2.imread(r'C:\Users\Administrator\Pictures\paisagem.jpg')

# Agora você pode convertê-lo para escala de cinza
img_cinza = cv2.cvtColor(img_colorida, cv2.COLOR_BGR2GRAY)

# Converte a imagem para escala de cinza
img_cinza = cv2.cvtColor(img_colorida, cv2.COLOR_BGR2GRAY)

# Exibe a imagem colorida
cv2.imshow('Imagem Colorida', img_colorida)

# Exibe a imagem em escala de cinza
cv2.imshow('Imagem em Escala de Cinza', img_cinza)

# Aguarda uma tecla ser pressionada para fechar as janelas
cv2.waitKey(0)
cv2.destroyAllWindows()