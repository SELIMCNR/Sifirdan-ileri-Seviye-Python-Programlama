print(5000-(5000*0.27))
print(4000-(4000*0.27))

maasA = 5000
maasB = 4000
vergi = 0.27

print(maasA-(maasA*vergi))
print(maasB-(maasB*vergi))

#Değişken Tanımlama Kuralları
# 1) Rakam ile başlayamaz.   #1DEGİSKEN=54   HATALI
# 2) Büyük küçük harf duyarlılığı vardır. #DEGİS=75 degis85 farklı degiskenler
# 3) Türkçe karakter kullanılmaz.   çegis =75  üser=75 HATALI 
# 4) Boşluk bırakılmaz.            s 75 b c = 100 HATALI
# 5) Özel karakterler kullanılamaz.  ?ax = 85 HATALI
# 6) Değişken adı tanımlamak için keyword'ler kullanılamaz. switchbreak = 85 HATALI
# 7) Değişken adı içerisinde sadece harf, rakam ve alt çizgi karakteri kullanılabilir. _75 = 85 DOGRU

yas = 20
_age = 35

x=1    #int
y=5.1 #float
name = "Çınar" #string
isStudent = True #bool

print(yas+_age)
print(type(yas))  #değişkenin tipini gösterir.

a = "10"
b = "400"
print(a+b) #10400
print(type(a)) #string
print(type(b)) #string

firstname = "Selim"
lastnmame = "Çınar"
print(firstname + " " + lastnmame) #Selim Çınar

x,y,name,isStudent = (5,2.8,"Çınar",True)

print(type(x))
print(type(y))

"""
       1-Bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz.
        Müşteri adı
        Müşteri soyadı 
        Müşteri ad + soyad
        Müşteri cinsiyet
        Müşteri tc kimlik
        Müşteri doğum yılı
        Müşteri adres bilgisi
        Müşteri yaşı


"""
#1.soru 
musteriAdi = "Selim"
musteriSoyadi = "Çınar"
musteriAdiSoyadi =musteriAdi+" "+musteriSoyadi
musteriCinsiyet = True #Erkek
musteriTcKimlik = "123456789"
musteriDogumYili = 2000
musteriAdres = "Kahramanmaraş"
musteriYaşı = 2023-musteriDogumYili
print("------------------------------")
print("Adi : "+musteriAdiSoyadi)
print("Yasi : "+str(musteriYaşı))
print("Cinsiyeti : "+str(musteriCinsiyet))
print("Tc kimlik:"+musteriTcKimlik)
print("Adres: "+musteriAdres)


"""

"""




