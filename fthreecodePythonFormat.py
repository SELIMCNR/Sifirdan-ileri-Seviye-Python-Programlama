name = "Çınar"
surname = "Fenerbahçe"
age = 25

print('My name is {} {}'.format(name,surname))
print('My name is {0} {1}'.format(name,surname))
print('My name is {1} {0}'.format(name,surname))
print('My name is {s} {n}'.format(n=name,s=surname))
print("My name is {} {} and I'm {} years old".format(name,surname,age))
print("My name is {} {} and I'm {} years old".format(name,name,name))

result = 400/700
print("The result is {}".format(result))
print("The result is {r:1.3}".format(r=result))

print(f"My name is {name} {surname} and I'm {age} years old")

#String demo uygulama

website = "https://www.btkakademi.gov.tr/"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır ?
result = len(course)
length = len(website)

# 2- 'website' içinden www karakterlerini alın
result= website[8:11]
# 3- 'website' içinden gov karakterlerini alın
result= website[19:22]
result = website[length-3:length]

# 4- 'website' içinden ilk 15 ve son 15 karakterlerini alın
result=website[0:15]
result=website[-15:]
result=website[-15:-1]
# 5- 'course' ifadesindeki karakterleri tersten yazdırın
result=course[::-1]

name , surname , age , job = 'Yusuf' , 'Çınar' , 24 , 'mühendis'

# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın
# 'Benim adım Yusuf Çınar, Yaşım 24 ve mesleğim mühendis.'
result=f'Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}.'
result = "Benim adım " + name + " " + surname + ", Yaşım " + str(age) + " ve mesleğim " + job + "."
result = "Benim adım {0} {1}, Yaşım {2} ve mesleğim {3}.".format(name,surname,age,job)
# 7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin    
s = 'Hello world'
s = s[0:6] + 'W' + s[-4:]
result = s

# 8- 'abc' ifadesini yan yana 3 defa yazdırın
result='abc ' * 3
print(result)





