#method

list1 = [1,2,3]
list1.append(4)
list1.pop()
print(list1)
print(type(list1)) #class list

myString = "Hello"
print(type( myString)) #class string str
print(myString.upper()) #upper() methodur fonksiyondur


#function geriye değer döndürmeyen
def sayHello(): #fonksiyon tanımlama
    print("Hello")

sayHello()    #fonksiyon çalıştırma
sayHello()

#parametreli fonksiyon
def sayHello(name = "user"):
    print("Hello " + name)

sayHello("Selim")
sayHello("Çınar")

#return değer döndüren fonksiyon
def sayHello(name = "user"):
    return "Hello " + name

msg = sayHello("Selim")
print(msg)


def total(num1,num2):
    return num1 + num2
result=total(10,20)
result=total(15,20)
print(result)

def yasHesapla(dogumYili):
    return 2023 - dogumYili

ageSelim = yasHesapla(2000)
ageCinar = yasHesapla(1900)
ageName = yasHesapla(2013)
print(ageSelim,ageCinar,ageName)


def EmekliligeKacYilKaldi(dogumYili,isim):
    
    '''
    DOCSTRING : Dogum yiliniza gore emekliliginize kac yil kaldi
    INPUT : Dogum yili
    OUTPUT : Hesaplanan yil bilgisi
    '''

    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if emeklilik>0:
        print(f"Emekliliğinize {emeklilik} yıl kaldı")
    else:
        print("Zaten emekli oldunuz")

EmekliligeKacYilKaldi(2000,"Selim")
EmekliligeKacYilKaldi(1950,"name")
EmekliligeKacYilKaldi(1900,"surname")

print(help(EmekliligeKacYilKaldi)) #fonksiyonun docstringini gösterir

list2 = [1,2,3]
print(help(list2.append)) #fonksiyonun docstringini gösterir      