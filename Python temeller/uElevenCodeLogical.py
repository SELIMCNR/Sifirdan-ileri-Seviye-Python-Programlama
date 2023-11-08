x = 5

result =  5 < x < 10
hak = 5
devam ='e'

# and 
result = x>5 and x<10 
result = (hak>0) and (devam=='e')

# or 
result = (x>0) or (x%2==0)

# not
result = not(x>0)

# x, 5-10 arasında olan bir çift sayı mı?
result = (x>5) and (x<10) and (x%2==0)
print(result)

# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
sayi = float(input('Sayı: '))
result = (sayi>0) and (sayi<100)
print(f'Sayı 0-100 arasında mı: {result}')

# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
sayi = float(input('Sayı: '))
result = (sayi>0) and (sayi%2==0)
print(f'Sayı pozitif çift sayı mı: {result}')

# 3- Email ve parola bilgileri ile giriş kontrolü yapınız.
email = 'email@sadik'
password = '12345'

girilenEmail = input('Email: ')
girilenPassword = input('Parola: ')

result = (email==girilenEmail) and (password==girilenPassword)
print(f'Giriş bilgileri doğru mu: {result}')

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

result = (a>b) and (a>c)
print(f'a en büyük sayıdır: {result}')
result = (b>a) and (b>c)
print(f'b en büyük sayıdır: {result}')
result = (c>a) and (c>b)
print(f'c en büyük sayıdır: {result}')

# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#     Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
vize1 = float(input('1. Vize: '))
vize2 = float(input('2. Vize: '))
final = float(input('Final: '))

ortalama = (((vize1+vize2)/2)*0.6) + (final*0.4)
result = (ortalama>=50) and (final>=50)

print(f'Ortalama: {ortalama} ve dersten geçme durumu: {result}')


# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#   Formül : (Kilo / boy uzunluğunun karesi)
#   Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#   0-18.4    => Zayıf
#   18.5-24.9 => Normal
#   25.0-29.9 => Fazla Kilolu
#   30.0-34.9 => Şişman (Obez)

name = input('Adınız: ')
kg = float(input('Kilonuz: '))
hg = float(input('Boyunuz: '))
index = (kg) / (hg**2)
zayıf = (index>=0) and (index<=18.4)
normal = (index>=18.5) and (index<=24.9)
kilolu = (index>=25.0) and (index<=29.9)
şişman = (index>=30.0) and (index<=34.9)

print(f'{name} Kilo indeksiniz: {index} ve kilo değerlendirmeniz: {zayıf}')
print(f'{name} Kilo indeksiniz: {index} ve kilo değerlendirmeniz: {normal}')
print(f'{name} Kilo indeksiniz: {index} ve kilo değerlendirmeniz: {kilolu}')
print(f'{name} Kilo indeksiniz: {index} ve kilo değerlendirmeniz: {şişman}')

#Identity Operator : İs obje adres önemli
x = y = [1,2,3]
z = [1,2,3]
print(x==y)
print(x==z)
print(x is y)
print(x is z)

#Membership Operator : in değer önemli
x = [1,2,3]
y = [2,4]
print(x in y)

del x[2]
y[1] =1
y.reverse()
print(x==y)
print(x is y)
print(x is not y)
x = ['apple', 'banana']
print('banana' in x)

name = 'Çınar'
print('a' in name)
print('a' not in name)

