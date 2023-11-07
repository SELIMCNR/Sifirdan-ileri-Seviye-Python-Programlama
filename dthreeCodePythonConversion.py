x = input('İlk sayı : ')
y = input("İkinci sayı : ")

print("Tipi : "+str(type(x)))
print("Tipi : "+str(type(y)))

toplam = int(x) + int(y)
print(toplam)

#Type Conversion
x = 50      # int
y = 2.59     # float
name = "Çınar" # str
isOnline = True # bool
print(type(x))
print(type(y))
print(type(name))
print(type(isOnline))

# int to float
x = float(x)
print(x)
print(type(x))

#float to int 
y = int(y)
print(y)
print(type(y))

result = x+y
print(result)
print(type(result))

result = str(x)+str(y)
print(result)
print(type(result))

# bool to str
isOnline = str(isOnline)
print(isOnline)
print(type(isOnline))

# Demo uygulama conversion
'''
    Daire alanı : πr^2
    Daire çevresi : 2πr
    * yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız. (pi: 3.14)

'''
r = int(input("Yaricap  : "))
pi = 3.14
alan = pi*r**2
cevre = 2*pi*r
print("Alan : "+str(alan)+" Çevre : "+str(cevre))


# Kare , Dikdörtgen , Silindir
# Kare Alan : a*a
# Kare Çevre : 4*a
karekenar = int(input("Karenin kenar uzunluğu : "))
karealan = karekenar**2
karecevre = 4*karekenar
print("Karenin alanı : "+str(karealan)+" Karenin çevresi : "+str(karecevre))

# Dikdörtgen Alan : a*b
# Dikdörtgen Çevre : 2*(a+b)
dikdörtgenkısakenar = int(input("Dikdörtgenin kısa kenar uzunluğu : "))
dikdörtgenuzunkenar = int(input("Dikdörtgenin uzun kenar uzunluğu : "))
dikdörtgenalan = dikdörtgenkısakenar*dikdörtgenuzunkenar
dikdörtgencevre = 2*(dikdörtgenkısakenar+dikdörtgenuzunkenar)
print("Dikdörtgenin alanı : "+str(dikdörtgenalan)+" Dikdörtgenin çevresi : "+str(dikdörtgencevre))

# Silindir Alan : 2πr(r+h)
# Silindir Hacim : πr^2h
silindiryaricap = int(input("Silindirin yarıçapı : "))
silindiryukseklik = int(input("Silindirin yüksekliği : "))
silindiralan = 2*pi*silindiryaricap*(silindiryaricap+silindiryukseklik)
silindirhacim = pi*silindiryaricap**2*silindiryukseklik
print("Silindirin alanı : "+str(silindiralan)+" Silindirin hacmi : "+str(silindirhacim))

# 1- Kullanıcıdan vize(%60) ve final(%40) notunu alıp ortalama hesaplayınız.
vize = int(input("Vize notunuz : "))
final = int(input("Final notunuz : "))
ortalama = vize*0.6+final*0.4
print("Ortalamanız : "+str(ortalama))