import cv2

# Carregar a imagem
img = cv2.imread(r'C:\Users\Administrator\Pictures\paisagem.jpg')  # Carrega em escala de cinza

# Aplicar o detector de bordas Canny
canny = cv2.Canny(img, 100, 200)

# Exibir a imagem com as bordas detectadas
cv2.imshow('Imagem com Bordas', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()