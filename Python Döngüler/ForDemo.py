
sayilar = [1,3,5,7,9,12,19,21]

# 1-Sayilar listesindeki hangi sayılar 3'ün katıdır ?
for sayi in sayilar:
    if (sayi % 3 == 0):
        print(sayi)


# 2-Sayilar listesindeki sayıların toplamı kaçtır ?
toplam = 0
for sayi in sayilar:
    toplam = toplam + sayi
    print(toplam)

# 3-Sayilar listesindeki tek sayıların karesini alınız.

for sayi in sayilar:
    if (sayi % 2 == 1):
        print(sayi**2)
sehirler = ['kocaeli','istanbul','ankara','izmir','rize']        
# 4- Şehirlerden hangileri en fazla 5 karakterlidir ?
for sehir in sehirler:
    if (len(sehir) <= 5):
        print(sehir)
urunler = [
    {'name':'samsung s6','price':'3000'},
    {'name':'samsung s7','price':'4000'},
    {'name':'samsung s8','price':'5000'},
    {'name':'samsung s9','price':'6000'},
    {'name':'samsung s10','price':'7000'}   
]
# 5- Ürünlerin fiyatları toplamı nedir ?
toplam =0
for urun in urunler :
   fiyat = int(urun['price'])
   toplam = toplam + fiyat
print(toplam)

# 6- Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz.
for urun in urunler:
    if (int(urun['price']) <= 5000):
        print(urun['name']) 

# 7- Tek sayıları döngü içinde ekrana yazdırınız.
num =range(0,50)
for n in num:
    if (n % 2 == 1):
        print(n)
# 8-Çift sayıları döngü içinde ekrana yazdırınız.
for n in num:
    if (n % 2 == 0):
        print(n)
# 9- 0-50 arasındaki tek sayıların toplamı nedir ?
toplam = 0
for n in num :
    if (n % 2 == 1):
        toplam = toplam + n
print(toplam)
# 10- 0-50 arasındaki çift sayıların toplamı nedir ?
toplam = 0
for s in num :
    if (s % 2 == 0):
        toplam = toplam + s
print(toplam)

# Rastgele 50 sayıdan sayı bilme 
import random
sayi = random.randint(1,50)
sayac=0

tutulansayi = int(input('sayi tutunuz:'))
while True:
    if (sayi == tutulansayi):
        print('tebrikler',sayac,'defada bildiniz')
        sayac = sayac + 1
        break
    elif (sayi > tutulansayi):
        print('yukarı')
        sayac = sayac + 1
        tutulansayi = int(input('sayi tutunuz:'))
    else:
        print('aşağı')
        sayac = sayac + 1
        tutulansayi = int(input('sayi tutunuz:'))


