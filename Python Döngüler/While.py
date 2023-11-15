
i = 0

while i <50:
    print(i)
    i +=1


i=100
while i>0:
    print(i)
    i -=1


i= 0 
while i<100:
    i+=1
    if(i%2==0):
        print(i)

i = 0 
while i<100:
    i+=1
    if(i%2==1):
        print(i)

i = 0
toplam = 0
while i<100:
    if(i%2==1):
        toplam = toplam + i
    i +=1
print(toplam)

karakter = 'A'
while karakter< 'Z':
    print(karakter)
    karakter=chr(ord(karakter)+1)  #ord() karakterin ascii karşılığını verir. chr() ise ascii karşılığını karaktere çevirir.