website = "https://www.btkakademi.gov.tr/"
course = "Python Programlama Dili Kursu"

# 1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
result = ' Hello World '.strip()
result = ' Hello World '.lstrip()
result = ' Hello World '.rstrip()

# 2- 'https://www.btkakademi.gov.tr' içindeki btkakademi bilgisi haricindeki her karakteri silin.
result = website.strip('htps:/w.govtr')

# 3- 'course' karakter dizisinin tüm karakterlerini küçük harf yapın.
result = course.lower()
result = course.upper()
result = course.title()

# 4- 'website' içinde kaç tane a vardır ? 
result = website.count('a')
result = website.count('a',0,10)

# 5- 'website' "www" ile başlayıp "gov" ile bitiyor mu?
result = website.startswith('www')
result = website.endswith('gov')

# 6- 'website' içinde '.gov' ifadesi var mı?
result = website.find('.gov')



# 7- 'course' içindeki karakterlerin hepsi alfabetik mi?
result = course.isalpha()
result = course.isdigit()
result = '123'.isdigit()

# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
result = 'Contents'.center(50,'*')

# 9- 'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
result = course.replace(' ','-')

# 10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
result = 'Hello World'.replace('World','There')
# 11- 'course' karakter dizisini boşluk karakterlerinden ayırın.    
result = course.split(' ')

print(result)

# 12- 'Merhaba' ifadesini 5 defa yan yana yazdırın.
print('Merhaba '*5)