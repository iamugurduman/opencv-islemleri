
import numpy as np

import cv2

image=cv2.imread(r"C:\Users\duman\OneDrive\Desktop\Projects_Deneme\Deneme\OpenCv-Islemleri\shrek.png")

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)#görseli griye çevirdik

blur=cv2.GaussianBlur(gray,(5,5),0)#gri görsele blur ekledik,etrafındaki 5x5 matrislerin ağırlıklı ortalamasını alıp o değere göre blur ekleniyor.

canny=cv2.Canny(blur,50,150)#blurlu görsele kenar çizgi eklemesi,pix>150 kesin kenar çiz.pix<50,çizme.


def autocanny(blur,sigma=0.33):#kenar ekleme fonksiyonu oluşturduk
    median=np.median(blur)
    lower=int(max(0,(1.0-sigma)*median))
    upper=int(min(255,(1.0+sigma)*median))
    canny=cv2.Canny(blur,lower,upper)
    return canny

wide=cv2.Canny(blur,10,200)
tight=cv2.Canny(blur,200,230)
auto=autocanny(blur)
cv2.imshow("blurred",blur)
cv2.imshow("edges",np.hstack([wide,tight,auto]))#3 görselin tek bir çerçevede görünmesini sağladık
    
cv2.waitKey(0)
cv2.destroyAllWindows()#s
