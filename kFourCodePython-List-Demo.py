names = ['Michael', 'Bob', 'Tracy', 'Adam']
years = [1991, 1992, 1993, 1994]

# 1- "Cenk" ismini listenin sonuna ekleyiniz.
names.append("Cenk")
# 2- "Sena" değerini listenin başına ekleyiniz.
names.insert(0,"Sena")
# 3- "Adam" ismini listeden siliniz.
names.remove("Adam")
# 4- "Adam" isminin indeksi nedir ?
result = names.index("Adam")
# 5- "Ali" listenin bir elemanı mıdır ?
result = "Ali" in names
# 6- Liste elemanlarını ters çevirin.
names.reverse()
# 7- Liste elemanlarını alfabetik olarak sıralayınız.
names.sort()
# 8- years listesini rakamsal büyüklüğe göre sıralayınız.
years.sort()
# 9- str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
str = "Chevrolet,Dacia"
result = str.split(",")
# 10- years dizisinin en büyük ve en küçük elemanı nedir ?
result = min(years)
result = max(years)
# 11- years dizisinde kaç tane 1994 değeri vardır ?
result = years.count(1994)
# 12- years dizisinin tüm elemanlarını siliniz.
years.clear()
# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
markalar = []
marka = input("Marka: ")
markalar.append(marka)
marka = input("Marka: ")
markalar.append(marka)
marka = input("Marka: ")
markalar.append(marka)
result = markalar
# 14- Liste elemanlarını ekrana yazdırınız.
print(result)

