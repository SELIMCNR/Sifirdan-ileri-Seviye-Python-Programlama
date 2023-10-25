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
