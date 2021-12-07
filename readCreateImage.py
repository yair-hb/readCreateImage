import cv2
import os 

path = r'C:\Users\OptiPlex\Desktop\TODO YAIR\PYTHON 3 openCV\readCreateImage\im.jpg'
imagen = cv2.imread(path, 0)
window_name = 'Lectura de imagen'
nombre = "imagengris.jpg"
cv2.imshow(window_name,imagen)
cv2.imwrite("nombreimagengris.jpg", imagen)
cv2.waitKey(2000)
cv2.destroyAllWindows()
