import cv2

# Carregar a imagem
img = cv2.imread(r'C:\Users\Administrator\Pictures\paisagem.jpg')

# Redimensionar a imagem para 200x200 pixels
img_resized = cv2.resize(img, (200, 200))

# Exibir a imagem redimensionada
cv2.imshow('Imagem Redimensionada', img_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()