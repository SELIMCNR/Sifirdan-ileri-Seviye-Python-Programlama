# 1- "Bmw,Mercedes,Opel,Mazda" elemanlarına sahip bir liste oluşturunuz.
arabalar=["Bmw","Mercedes","Opel","Mazda"]

# 2- Liste kaç elemanlıdır ?
result = len(arabalar)
# 3- Listenin ilk ve son elemanı nedir ?
result = arabalar[0]
result = arabalar[3]
# 4- Mazda değerini Toyota ile değiştirin.
arabalar[-1]="Toyota"
result = arabalar
# 5- Mercedes listenin bir elemanı mıdır ?
result = "Mercedes" in arabalar
# 6- Listenin -2 indeksindeki değer nedir ?
result = arabalar[-2]
# 7- Listenin ilk 3 elemanını alın.
result = arabalar[:3]
result = arabalar[0:3]
result = arabalar[-2:]

# 8- Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin.
arabalar[-2:] = ["Toyota","Renault"]
result = arabalar

# 9- Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
result = arabalar + ['Audi','Nissan']
# 10- Listenin son elemanını silin.
del arabalar[-1]
result = arabalar

# 11- Liste elemanlarını tersten yazdırın.
result = arabalar[::-1]
# 12- Aşağıdaki verileri bir liste içinde saklayınız.
    # studentA: Yiğit Bilgi 2010, (70,60,70)
    # studentB: Sena Turan  1999, (80,80,70)
    # studentC: Ahmet Turan 1998, (80,70,90)
studentA = ["Yiğit","Bilgi",2010,[70,60,70]]
studentB = ["Sena","Turan",1999,[80,80,70]]
studentC = ["Ahmet","Turan",1998,[80,70,90]]
students = [studentA,studentB,studentC]
# 13- Liste elemanlarını ekrana yazdırın.
result = students[0]
result = students[2]
result = students[0][0]
result = students[0][1]
ortalama =(studentA[3][0]+studentA[3][1]+studentA[3][2])/3
ortalama = ortalama.__round__(2)
result = f"{studentA[0]} {studentA[1]} {2023-studentA[2]} yaşında ve not ortalaması {ortalama}" 

print(arabalar)
print(result)

#14 - Aşağıdaki bilgileri liste içinde saklayınız.
    # ListA: AList BList CList
    # ListB: SList TList  Klist
    # ListC: XList YList  ZList

ListA = ["AList","BList","CList"]
ListB = ["SList","TList","KList"]
ListC = ["XList","YList","ZList"]
ListD = [ListA,ListB,ListC]
print(ListD)


list15 = ["myone","mytwo","mythree"]

print(list15[::-1]) # listeyi ters çevirir.
print(list15[0:2]) # listeyi 0. indexten 2. indexe kadar yazdırır.
print(list15[0:3:2]) # listeyi 0. indexten 3. indexe kadar 2 şer 2 şer yazdırır.
list15[0:2] = ["myfour","myfive"] # listeyi 0. indexten 2. indexe kadar olan kısmı değiştirir.
print(list15)
list15[-1] = "mysix" # listeyi sondan bir önceki indexi değiştirir.
print(list15)
print("myone" in list15) # listede myone var mı diye kontrol eder.
