# username ,password => database

# 'sadik', '123456'

a,b,c,d = 5,5,10,4
pasword = '1234'
username = 'sadik'

result = a == b
result = a == c
result = ('sdk' == username)
result = ('sadik' == username)
result = (a != b)
result = (a != c)
result = (a > b)
result = (a < c)
result = (a >= c)
result = (a<= b)
result = (True == 1)
result = (False == 0)
result = False + True + 40

print(result)

# Demo karşılaştırma operatörleri

# 1- Girilen 2 sayının büyük olanını ekrana yazdırın
a = int(input("1.sayı: "))
b = int(input("2.sayı: "))
result = (a>b)
print(f"{a} sayısı {b} sayısından büyüktür: {result}")
# 2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın
vize1 = float(input("1.vize: "))
vize2 = float(input("2.vize: "))
final = float(input("final: "))
ortalama = (((vize1+vize2)/2)*0.6) + (final*0.4)
print(f"ortalama: {ortalama} ve dersten geçme durumu: {ortalama>=50}")
# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın
sayi = int(input("sayı: "))
print(f"{sayi} sayısı çift mi: {sayi%2==0}")
# 4- Girilen bir sayının negatif pozitif durumunu yazdırın
sayi = int(input("sayı: "))
print(f"{sayi} sayısı pozitif mi: {sayi>0}")
# 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
# (email : email@sadikturan parola : 123456)
email = input("email: ")
password = input("password: ")
result = (email == "email@sadikturan" and password == "123456")
print(result)
