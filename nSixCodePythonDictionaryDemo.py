'''
    ogrenciler = {
        '1': {
            'ad': 'A',
            'soyad': 'Y',  
            'telefon': '555 555 55 55'
        },
        '2': {
            'ad': 'C',
            'soyad': 'Y',
            'telefon': '555 555 55 55'
        },
        '3': {
            'ad': 'E',
            'soyad': 'Y',
            'telefon': '555 555 55 55'
        }
        }
        1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.
        2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.


'''
ogrenciler = {}
number = input("How many students will you add? ")
for i in range(int(number)):
    name = input("Name: ")
    surname = input("Surname: ")
    phone = input("Phone: ")
    ogrenciler[i+1] = {
        'name': name,
        'surname': surname,
        'phone': phone
    }
print(ogrenciler)
number = input("Which student do you want to see? ")
print(f"Name: {ogrenciler[int(number)]['name']} Surname: {ogrenciler[int(number)]['surname']} Phone: {ogrenciler[int(number)]['phone']}")