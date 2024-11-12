import cv2

imagen= cv2.imread('imagen.png')
gray=cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
canny=cv2.Canny(gray,10,150)

cnts, _ = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(imagen, cnts,-1,(0,255,0),2)
for c in cnts:
    epsilon=0.01*cv2.arcLength(c,True)
    aprox=cv2.approxPolyDP(c,epsilon, True)
    x,y,w,h=cv2.boundingRect(aprox)
    if len(aprox)==3:
        cv2.putText(imagen,'triangulo', (x,y-5),1,1,(0,255,0),1)
    if len(aprox)==4:
        aspect_ratio=float(w)/h
        print('aspect_ratio= ',aspect_ratio)
        if aspect_ratio == 1:
            cv2.putText(imagen,'cuadrado',(x,y-5),1,1,(0,255,0),1)
        else:
            cv2.putText(imagen,'rectangulo',(x,y-5),1,1,(0,255,0),1)
    if len(aprox)==5:
        cv2.putText(imagen,'pentagono',(x,y-5),1,1,(0,255,0),1)
    if len(aprox)==6:
        cv2.putText(imagen,'hexagono',(x,y-5),1,1,(0,255,0),1)
    cv2.drawContours(imagen, [c],0,(0,255,0),2)
    if len(aprox)>10:
        cv2.putText(imagen,'circulo',(x,y-5),1,1,(0,255,0),1)
    cv2.imshow('imagen',imagen)
    cv2.waitKey(0)
cv2.imshow('imagen',imagen)
cv2.imshow('canny', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
