import cv2

# Carrega a imagem
img = cv2.imread(r'C:\Users\Administrator\Pictures\paisagem.jpg')

# Cria uma janela para exibir a imagem
cv2.imshow('Minha Paisagem', img)

# Aguarda até que uma tecla seja pressionada
cv2.waitKey(0)

# Fecha todas as janelas
cv2.destroyAllWindows()