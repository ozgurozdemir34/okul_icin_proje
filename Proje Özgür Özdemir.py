import sqlite3
vt=sqlite3.connect('C:/Users/okul/Desktop/yeni.db')
im = vt.cursor()
sql="""CREATE TABLE IF NOT EXISTS 'veri'
(Şirket,Şehir,Şube)"""
değergir="""INSERT INTO 'veri' VALUES
('Özgür Bilgisayar','Muğla','Menteşe')"""
im.execute(sql)
im.execute(değergir)
vt.commit()
im.execute("""SELECT * FROM 'veri'""")
veriler=im.fetchall()
print(veriler)
while True:
    def dolarfiyat(a,b,c,d,e):
        return a+b+c+d+e
    def tlfiyat(a,b):
        return a*b
    def yanürün(a,b,c):
        return a+b+c
    karar=input("Dizüstü mü yoksa masaüstü mü almak istiyorsunuz:\n")
    if karar=="masaüstü":
        dizüstüfiyat=0
        def masaüstütopla(a,b,c,d,e,f,g):
            return a+b+c+d+e+f+g
            
        marka=input("Ryzen mi yoksa İntel mi tercih edeceksiniz(r/i):\n")
        if marka=="i":
             anakart=input("B660($172.00), H610($85) ,Z690($330) modellerinden birini seçiniz:\n")
             if anakart=='B660' or 'H610' or 'Z690':
                 if anakart=="Z690":
                     anakart=330
                 elif anakart=="H610":
                     anakart=85
                 elif anakart=="B660":
                     anakart=172            
                 işlemci=input("""İ5-12600K($320) ,İ3-12100($120),İ7-12700K($385),İ9-12900K($650) işlemcilerinden birini seçiniz
                               (seri adı yazmanız yeterlidir)(İ7 ve İ9 ile Z690 kulllanılması tavsiye edilir):\n""")              
                 if işlemci=="İ5":
                     işlemci=320
                 elif işlemci=="İ3":
                     işlemci=120
                 elif işlemci=="İ7":
                     işlemci==385
                 elif işlemci=="İ9":
                     işlemci=650
               
            
        if marka=="r":
            anakart=input("B450($60), B550($115), X570($170)  modellerinden birini seçiniz:\n")
            if anakart=="B450" or "B550" or "X570": 
                if anakart=="B450":
                    anakart=60
                elif anakart=="B550":
                    anakart=115
                elif anakart=="X570":
                    anakart=170
                
                işlemci=input(""""Ryzen 5 5500($160), Ryzen 5 5600X($230), Ryzen 7 5700X($300), Ryzen 9 5900X($450) işlemcilerinden birini seçiniz
                        (model adı yazmanız yeterlidir)(Ryzen 9 ile X570 kulllanılması tavsiye edilir):\n""")    
                if işlemci=="5500":
                    işlemci=160
                elif işlemci=="5600X":
                    işlemci=230
                elif işlemci=="5700X":
                    işlemci=300
                elif işlemci=="5900X":
                    işlemci=450
            
            
        ekrankartı=input(""""Aşağıdaki ekran kartlarından numarasına göre birini seçiniz

     1-RTX 2060($350)
     2-RTX 2070($500)
     3-RTX 2080($700)
     4-RX 5700($400)
     5-RX 580($230)
     6-R7 240($50)\n""")
        if ekrankartı=="1":
            ekrankartı=350
        if ekrankartı=="2":
            ekrankartı=500   
        if ekrankartı=="3":
            ekrankartı=700
        if ekrankartı=="4":
            ekrankartı=400
        if ekrankartı=="5":
            ekrankartı=230
        if ekrankartı=="6":
            ekrankartı=50
            
        ram=input("""Aşağıdaki ramlerden birini numarasına göre seçiniz

       1-8GB($40)

      2-16GB($70)

      3-32GB($130)

      4-4GB($20)\n""")
      
           
        if ram=="1":
           ram=40
        if ram=="2":
           ram=70
        if ram=="3":
           ram=130
        if ram=="4":
           ram=20
        print("Güçlü sistemler için güçlü güç kaynaklarının gerektiğini göz önünde bulundurunuz\n")
        psu=input("""Numarasına göre güç kaynaklarından birini seçiniz:
                  1-500W($35)

                  2-600W($45)

                  3-700W($70)

                  4-400W($30)\n""")
        if psu=="1":
            psu=35
        if psu=="2":
            psu=45
        if psu=="3":
            psu=70
        if psu=="4":
            psu=30
               
        kasa=input("""Numarasına göre kasalardan birini seçiniz:
                   1-Mid Tower($90)

                   2-Micro ATX($60)\n""")
        if kasa=="1":
            kasa=90
        if kasa=="2":
            kasa=60
        hdd=input("""Aşağıdaki HDD’lerden birini seç

     1-250GB($30)

     2-500GB($35)

     3-1TB($40)\n""")              
        
        if hdd=="1":
            hdd=30
        if hdd=="2":
            hdd=35
        if hdd=="3":
            hdd=40
        try:
         sayı1=int(işlemci)
         sayı2=int(anakart)
         sayı3=int(ekrankartı)
         sayı4=int(ram)
         sayı5=int(psu)
         sayı6=int(kasa)
         sayı7=int(hdd)
         masaüstüfiyat=masaüstütopla(sayı1,sayı2,sayı3,sayı4,sayı5,sayı6,sayı7)
         sözlük1={"İşlemci":sayı1,"Anakart":sayı2,"Ekran kartı":sayı3,"RAM":sayı4,"Güç kaynağı":sayı5,"Kasa":sayı6,"HDD":sayı7}
         print("Masaüstü donanımlarının fiyatları:")
         for i in sözlük1.items():             
             print(i)
        except ValueError:
            print("Hatalı seçim yaptınız lütfen tekrar deneyiniz")
    if karar=="dizüstü":
        masaüstüfiyat=0
        dizüstüfiyat=input("""Aşağıdaki dizüstü bilgisayarlardan birini numarasına göre seçiniz

      1-ASUS ROG Zephyrus 14" Gaming Laptop - AMD Ryzen 9 - 16GB Memory - NVIDIA GeForce RTX 3060 - 1TB SSD($1300)

      2-Lenovo Legion 5 15" Gaming Laptop - AMD Ryzen 7 5800H - NVIDIA GeForce RTX 3050 Ti - 8GB Memory - 512GB SSD ($950)

      3-Acer  Nitro 5 - 15.6" FHD 144Hz IPS Gaming Laptop – Intel 11th Gen i7 - GeForce RTX 3050Ti - 16GB DDR4 - 512GB SSD($1100)\n""")
            
        if dizüstüfiyat=="1":
            dizüstüfiyat=1300
        if dizüstüfiyat=="2":
            dizüstüfiyat=950
        if dizüstüfiyat=="3":
            dizüstüfiyat=1100
    os=input("İşletim sistemi kurulsun mu:\n (y/n)")      
    if os=="y":
        os=140
    if os=="n":
        os=0        
    fare=input("Fare almak ister misiniz:\n(y/n)")
    if fare=="y":
        fareseç=input("""Numaralara göre seçiniz:    
       1-Razer DeathAdder Oyuncu Faresi($30)

       2-TECKNET Oyuncu Faresi($25)

       3-Verbatim Standart Fare($7)\n""")
        if fareseç=="1":
            fareseç=30
        if fareseç=="2":
            fareseç==25
        if fareseç=="3":
            fareseç=7
    if fare=="n":
        fareseç=0
    klavye=input("Klavye almak ister misiniz:\n(y/n)")
    if klavye=="y":
        klavyeseç=input("""Numaralara göre seçiniz:
        1-Fiodo Oyuncu Klavyesi($25)

       2-Corsair K55 Oyuncu Klavyesi($40)

       3-Logitech Standart Klavye($15)\n""")
        if klavyeseç=="1":
            klavyeseç=25
        if klavyeseç=="2":
            klavyeseç=40
        if klavyeseç=="3":
            klavyeseç=15
    if klavye=="n":
        klavyeseç=0
    try:
        sayı1=int(fareseç)
        sayı2=int(klavyeseç)
        sayı3=int(os)
        yanürünler=yanürün(sayı1,sayı2,sayı3)
        sözlük2={"Fare":sayı1, "Klavye":sayı2, "İşletim sistemi":sayı3}
        print("Yan ürünlerin fiyatları:")   
        for i in sözlük2.items():                    
               print(i)
    except ValueError:
        print("Yanlış seçim yaptınız lütfen tekrar deneyiniz")
    try:
        sayı1=int(masaüstüfiyat)
        sayı2=int(dizüstüfiyat)
        sayı3=int(os)
        sayı4=int(fareseç)
        sayı5=int(klavyeseç)
        toplam=dolarfiyat(sayı1,sayı2,sayı3,sayı4,sayı5)
        print("Dolar cinsinden fiyat:",toplam)
    except ValueError:
        print("Yanlış seçim yaptınız lütfen tekrar deneyiniz")
    kur=(input("TL-Dolar kurunu giriniz:\n"))
    try:
        sayı1=(toplam)
        sayı2=float(kur)
        fiyat=tlfiyat(sayı1,sayı2)
        print("Toplam fiyat:",fiyat)
    except ValueError:
        print("Yanlış değer girdiniz")
    
    if fiyat>9999:
        print("Tebrikler TECKNET Oyuncu Faresi kazandınız")
    kart=input("Kart bilgilerinizi giriniz:\n")                    
    yöntem=input("Kargolansın mı yoksa gelip alacak mısnız(k/g):")
    if yöntem=="k":
        adres=input("Adresinizi giriniz:")
        bilgiler=[adres,kart]
        print("Bilgileriniz:",bilgiler)        
    if yöntem=="g":
        print("Sistem hazır olunca tarafınıza bilgilendirme yapılacaktır")
        bilgiler=[kart]
        print("Bilgileriniz:",bilgiler)
    soru=input("Sistemden çıkmak istiyor musunuz(y/n)")
    if soru=="y":
        class Kişi:
             def __init__(self, isim):
                self.isim = isim
        görevli=Kişi("Teslim alınacak görevli:Özgür Özdemir")
        print(görevli.isim)        
        break