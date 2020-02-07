#Arkadaslar master odevimiz sudur ;
#Bir dongu icerisinde random olacak sekilde iki tane  10x10’luk matris uretin ve bu matrislerin farklarini alin.
#Ve fark matrisinin diagonali,  -0.1 ile 0.1  arasinda olana kadar bu islemi tekrarlayin.
#Istenilen matris bulundugunda program dursun ve  toplam kac dongunun kuruldugunu,  ne kadar sure icinde buldugunu ve  istenilen  matrisi  print ile birlikte ekrana yazdiriniz...
#Tavsiye: 10 x 10 luk matrisin bulunmasi saatler surebilir. Bu yuzden algoritmanizin dogrulugunu test etmek icin once 4x4, 5x5 gibi kucuk matrislerde deneyebilirsiniz. Ve matris sayisisini arttirarak en son 10x10 u deneyebilirsiniz.
#Matris uretme islemini np.random.random((axb)) fonksiyonu ile yapabilirsiniz.(size kalmis) (edited) 



import numpy as np
import datetime as dt
n1=dt.datetime.now()

sayac=0
while(True):
    a=np.random.random((10,10))
    b=np.random.random((10,10))
   
    print("---------------------------------------------------------------------")
    print("a matrisi")
    print(a)
    print("b matrisi")
    print(b)
    print("fark matrisi")
    print(a-b)
    matris=np.diag(a-b)
    print(matris)
    kosul=matris<0.1
    kosul2=matris>-0.1
    sayac+=1
    if kosul.all() and kosul2.all():
        print("---------------------ISTENEN MATRIS----------------------------------")
        print(matris)
        print(sayac,"turda tamamlandi")
        n2=dt.datetime.now()
        print(n2-n1,"zamanda tamamlandi")
        break
 
