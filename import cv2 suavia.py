import cv2
import numpy as np

# Carregar a imagem
img = cv2.imread(r'C:\Users\Administrator\Pictures\paisagem.jpg')

# Aplicar um filtro gaussiano com kernel 5x5 e desvio padrão 0
kernel_size = 5
sigma = 0
blurred_img = cv2.GaussianBlur(img, (kernel_size, kernel_size), sigma)

# Exibir as imagens
cv2.imshow('Imagem Original', img)
cv2.imshow('Imagem Suavizada', blurred_img)
cv2.waitKey(0)
cv2.destroyAllWindows()