numbers=[]
for x in range(10):
    numbers.append(x)


numbers =[x for x in range(10)]
print(numbers)

for x in range (10):
    numbers.append(x**2)

numbers = [x**2 for x in range(10)]
print(numbers)

numbers= [x*x for x in range(10) if x%3==0]
print(numbers)

myString = []

for letter in myString:
    myString.append(letter)
print(myString)    

years = [1983,1999,2008,1956,1986]
ages = [2019-year for year in years]
print(ages)

results = [x if x%2==0 else 'TEK' for x in range(1,10)]
print(results)

results = []
for x in range(3):
    for y in range(3):
        results.append((x,y))   
print(results)        

numbers = [(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
print(numbers)

'''
    1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın.
    ** "random modülü" için "python random" şeklinde arama yapın.
    ** 100 üzerinden puanlama yapın. Her soru 20 puan.
    ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın.
'''
import random
sayi = random.randint(1,100)
can = int(input("Kaç hak kullanmak istersiniz: "))
hak = can
sayac = 0

while hak >0:
    hak -=1
    sayac+=1
    tahmin = int(input("tahmin: "))
    if sayi == tahmin:
        print(f"Tebrikler {sayac} bildiniz. Toplam puanınız{100 -(100/can) * (sayac-1)} ")
        break
    elif sayi > tahmin:
        print("yukarı")
    else :
        print("aşağı")

    if hak == 0 :
        print(f"Hakkınız bitti.tutulan sayı {sayi}")         

print(sayi)

'''
Soru : Girilen bir sayının asal olup olmadığını bulun.
** Asal sayı 1 ve kendisi hariç tam böleni olmayan sayılara denir.
'''

sayi = int(input("Sayı : "))
asalmi = True
if sayi ==1:
    print("1 sayısı asal değildir")

for i in range(2,sayi):
    if(sayi %i ==0):
        asalmi = False
        break

if asalmi:
    print("Sayı asaldır.")
else : 
    print("Sayı asal değildir.")    