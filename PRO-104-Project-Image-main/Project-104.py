# project 104

import cv2

img = cv2.imread("C:/Users/inno/Desktop/hardik coder all files/python1/PRO-104-Project-Image-main/solar-system.jpg")
cv2.waitKey(0)

cv2.putText(img,  
           "SUN",
           (40, 150),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           1,  
           (255,255,255)
           )
cv2.putText(img,  
           "Mercury",
           (100, 150),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           1,  
           (255,255,255)
           )
cv2.putText(img,  
           "venus",
           (200, 150),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           1,  
           (255,255,255)
           )
cv2.putText(img,  
           "Earth",
           (300, 150),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           1,  
           (255,255,255)
           )
cv2.putText(img,  
           "Mars",
           (400, 150),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           1,  
           (255,255,255)
           )
cv2.putText(img,  
           "Jupiter",
           (650, 150),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           1,  
           (255,255,255)
           )
cv2.putText(img,  
           "Saturn",
           (850, 150),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           1,  
           (255,255,255)
           )
cv2.putText(img,  
           "Uranus",
           (950, 150),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           1,  
           (255,255,255)
           )
cv2.putText(img,  
           "Neptune",
           (1050, 150),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           1,  
           (255,255,255)
           )
cv2.imwrite("Solar_systemwithname.jpg",img)


