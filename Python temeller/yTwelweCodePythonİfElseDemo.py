#1- Kullanıcıdan isim , yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz.
# Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır.
isim = input("isim: ")
yas = int(input("yaş: "))
egitim = input("eğitim: ")

if (yas >= 18):
    if (egitim == "lise" or egitim == "üniversite"):
        print(f"{isim} ehliyet alabilir")
    else:
        print(f"{isim} ehliyet alamaz eğitim durumu yetersiz")
else:
    print(f"{isim} ehliyet alamasın yaşınız uygun değil")    


#2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık gelen not bilgisini yazdırınız.
#    0 -24  => 0
#    25-44  => 1
#    45-54  => 2
#    55-69  => 3
#    70-84  => 4
#    85-100 => 5

yazili1 = float(input("1.yazılı: "))
yazili2 = float(input("2.yazılı: "))
sozlu = float(input("sözlü: "))
ortalama = (yazili1 + yazili2 + sozlu) / 3
if (ortalama >= 0 and ortalama <= 25):
    print(f"ortalamanız: {ortalama} notunuz 0")
elif (ortalama >= 25 and ortalama <= 44):
    print(f"ortalamanız: {ortalama} notunuz 1")
elif (ortalama >= 45 and ortalama <= 54):
    print(f"ortalamanız: {ortalama} notunuz 2")
elif (ortalama >= 55 and ortalama <= 69):
    print(f"ortalamanız: {ortalama} notunuz 3")
elif (ortalama >= 70 and ortalama <= 84):
    print(f"ortalamanız: {ortalama} notunuz 4")
elif (ortalama >= 85 and ortalama <= 100):
    print(f"ortalamanız: {ortalama} notunuz 5")
else:
    print("hatalı yanlış bilgi girdiniz.") 




#3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.
#    1. Bakım => 1. yıl
#    2. Bakım => 2. yıl
#    3. Bakım => 3. yıl
#    ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız..
#    *** datetime modülünü kullanmanız gerekiyor.
import datetime
tarih = input("aracınız hangi tarihte trafiğe çıktı  (2023/10/27) : " )
tarih = tarih.split("/")

trafigecikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now()
fark = simdi - trafigecikis
days = fark.days
if (days <= 365):
    print("1.servis aralığı")
elif (days > 365 and days <= 365*2):
    print("2.servis aralığı")
elif (days > 365*2 and days <= 365*3):
    print("3.servis aralığı")
else :
    print("hatalı süre girdiniz.")


'''
    1-Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
'''
sayi = int(input("sayı: "))
if (sayi > 0 and sayi < 100):
    print("sayı 0-100 arasında")
else:
    print("sayı 0-100 arasında değil")

'''   
    2-Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
'''
sayi = int(input("sayı: "))
if (sayi > 0):
   if(sayi % 2 == 0):
       print("sayı pozitif çift sayı")
   else:
       print("sayı pozitif ancak çift sayı değil")    
else:
    print("sayı pozitif çift sayı değil")


'''
    3-email ve parola bilgileri ile giriş kontrolü yapınız.
'''
email = "email@sadik.com"
password="123456"
girilenEmail = input("email: ")
girilenPassword = input("parola: ")
if (email == girilenEmail):
    if (password == girilenPassword):
        print("giriş başarılı")
    else:
        print("parola hatalı")
else:
    print("email hatalı")
'''    
    4- girilen 3 sayıyı büyüklük olarak karşılaştırınız.
    '''
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if (a>b) and (a>c):
    print(f"a en büyük sayı {a}")
elif (b>a)and (b>c):
    print(f"b en büyük sayı {b}")
elif (c>a) and (c>b):
    print(f"c en büyük sayı {c}")        


'''
    5-kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
    a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
    b-) Finalden 70 alındığında ortalamanın önemi olmasın.

'''
vize1 = float(input("1.vize : "))
vize2 = float(input("2.vize : "))
final = float(input("final :"))
ortalama = ((vize1 + vize2)/2)*0.6 + (final * 0.4)

if (ortalama >= 50):
    if (final >= 50):
        print(f"öğrencinin ortalaması {ortalama} ve geçti")
    else:
        print("öğrenci finalden 50 almalı")
else:
    print(f"öğrencinin ortalaması {ortalama} ve kaldı")        

'''    
    6- Kişinin ad,kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.,
    Formül: (Kilo/boy uzunluğunun karesi)
    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
    0-18.4    => Zayıf
    18.5-24.9 => Normal
    25.0-29.9 => Fazla Kilolu
    30.0-34.9 => Şişman (Obez)
'''
name = input('adınız: ')
kg = float(input('kilonuz: '))
hg = float(input('boyunuz: '))

index = (kg) / (hg ** 2)
if (index>0) and (index<=18.4):
    print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen zayıf")
elif (index>=18.5) and (index<=24.9):
    print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen normal")
elif (index>24.9) and (index<=29.9):
    print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen kilolu")
elif (index>29.9) and (index<=34.9):
    print(f"{name} kilo indeksin: {index} ve kilo değerlendirmen obez")





