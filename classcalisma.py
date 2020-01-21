# -*- coding: utf-8 -*-
"""
Çalışanların olduğu bir class oluşturulacak. Bu çalışanların isim, soyismi, yaş, maaş, email özellikleri olacak.

1)Çalışanları isme, soyisme, yaşa ve maaşa göre sort etme
2)verilen zam oranına göre bütün çalışanlara aynı oranda zam yapma(zam oranı parametre olacak)
3)zamların toplam maliyetini bulma
İşlemlerinin yapılabildiği kodlar perşembe gününe kadar github a girilecek.

"""


def siralama(liste):
    i = 0
    j = 0
    for index in range(len(liste)):
        j = index
        while (j > 0) and (liste[j - 1][0] > liste[j][0]):
            liste[j - 1], liste[j] = liste[j], liste[j - 1]
            j -= 1
    return liste


class Calisan():
    kisiler = list()
    isimler = list()
    soyisimler = list()
    yaslar = list()
    maaslar = list()
    maliyetler = list()

    def __init__(self, isim, soyisim, yas, maas):
        self.isim = isim
        self.soyisim = soyisim
        self.yas = yas
        self.maas = maas
        self.email = self.isim + self.soyisim + '@email.com'
        self.ekle()

    def ekle(self):

        self.kisiler = [self]

        for kisi in self.kisiler:
            self.isimler.append((kisi.isim, kisi))
            self.soyisimler.append((kisi.soyisim, kisi))
            self.yaslar.append((kisi.yas, kisi))
            self.maaslar.append((kisi.maas, kisi))

    def sort_isim(self):
        isim_sort = siralama(self.isimler)
        print("*****************************              ISIM             ******************************************")
        index = 0
        for isim in isim_sort:
            index += 1
            self.bilgiler(isim[1], index)

    def sort_soyisim(self):
        soyisim_sort = siralama(self.soyisimler)
        print("*****************************              SOYISIM              ******************************************")
        index = 0
        for soyisim in soyisim_sort:
            index += 1
            self.bilgiler(soyisim[1], index)

    def sort_yas(self):
        yas_sort = siralama(self.yaslar)
        print("*****************************                 YAS                   ******************************************")
        index = 0
        for yas in yas_sort:
            index += 1
            self.bilgiler(yas[1], index)

    def sort_maas(self):
        maas_sort = siralama(self.maaslar)
        print("*****************************                 MAAS                     ******************************************")
        index = 0
        for maas in maas_sort:
            index += 1
            self.bilgiler(maas[1], index)

    def bilgiler(self, kisi, index):
        print("""{}. KAYIT 
        ISIM    :{} 
        SOYISIM :{}     
        YAS     :{}         
        MAAS    :{}
        EMAIL   :{}
--------------------------------------------------------------------------------
            """.format(index, kisi.isim, kisi.soyisim, kisi.yas, kisi.maas, kisi.email))

    def maas_arttir(self, zam):

        for maas in self.maaslar:
            maas[1].maas = maas[0] + zam * maas[0]
            self.maliyetler += [maas[1].maas - maas[0]]

        print("Zam eklendi.")

    def zam_maliyet(self):
        
        print(self.maliyetler)
        print("Zamlarin toplam maliyeti= ", sum(self.maliyetler))


kayitlar = [
    Calisan("Naim", "Ucar", 38, 4000), Calisan("Salih", "Acar", 42, 2000), Calisan("Saim", "Derya", 23, 1280),
    Calisan("Mehmet", "Ucar", 33, 3400), Calisan("Saim", "Kackar", 28, 500), Calisan("Serkan", "Sevilen", 48, 2345),
    Calisan("Samet", "Aybaba", 18, 6547), Calisan("Derya", "Bolat", 34, 1000), Calisan("Berkay", "Turan", 58, 3400),
    Calisan("Ibrahim", "Baba", 44, 2550), Calisan("Hadise", "Hayal", 51, 3490), Calisan("Ceyda", "Zakir", 54, 1000),
    Calisan("Faruk", "Ucak", 37, 4000), Calisan("Nefise", "Uyma", 59, 3800), Calisan("Kerim", "Doven", 38, 2500),
    Calisan("Burhan", "Cacan", 39, 1459), Calisan("Gokhan", "Bilal", 21, 1900), Calisan("Hafiz", "Suleyman", 39, 1900),
    Calisan("Zeynel", "Abidin", 41, 1800), Calisan("Yavuz", "Ur", 28, 2200), Calisan("Ahmet", "Emin", 45, 2289),
    Calisan("Naim", "Umeyr", 188, 3422), Calisan("Nalan", "Ucares", 25, 777), Calisan("Ahmet", "Emin", 32, 4000),
]
for kayit in kayitlar:
    kayit = kayit

while (True):
    try:

        print("""

      SIRALAMA:                 
            ISIM     (I)             
            SOYISIM  (S)
            YAS      (Y)
            MAAS     (M)
      ZAM:
          ZAM YAPMA  (Z)
          MALIYET    (H)

        """)

        sec = input("seciminizi yapiniz : ").upper()
        if sec == "Q":
            break
        elif sec == "I":

            kayit.sort_isim()
        elif sec == "S":
            kayit.sort_soyisim()
        elif sec == "Y":
            kayit.sort_yas()
        elif sec == "M":
            kayit.sort_maas()
        elif sec == "Z":
            
            zam = float(input("zam oranini giriniz : "))
            kayit.maas_arttir(zam)
        elif sec == "H":
            kayit.zam_maliyet()
        else:
            print("lutfen seciminizi kontrol ediniz")

    except(ValueError):
        print("Lutfen islemi dogru yaptiginizdan emin olunuz...")



