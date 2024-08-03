import cv2
import numpy as np
import matplotlib.pyplot as plt


cb_img = cv2.imread("arco-ayacucho.jpg")

# Muestra la imagen resultante
#rgb = cv2.cvtColor(cb_img, cv2.COLOR_BGR2RGB)
# Extrae el canal rojo
b,g,r = cv2.split(cb_img)
cv2.imshow('RED',r)
cv2.waitKey(0)
#plt.destroyAllWindows()

# Set color map to gray scale for proper rendering.
#plt.imshow(cb_img, cmap="gray")
print(b)


w, h = r.shape

print(w,h)

negativo = np.zeros(r.shape,r.dtype)
for y in range (w):
  for x in range (h):
    negativo[y,x]=255-r[y,x]

cv2.imshow('NEGATIVO',negativo)
cv2.waitKey(0)

print(negativo)