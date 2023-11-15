def square(num): return num ** 2

result = square(5)


#Map istenirse listeye çevrilebilir ve metot içerisindeki işlemi yapar.
numbers = [1,3,5,9,10,4,2]
result = list(map(square,numbers))


#Map fonksiyonu ile for döngüsü kullanımı
for item in map(square,numbers):
    print(item)

#lambda fonksiyonu tek satırda fonksiyon tanımlamamızı sağlar.
result = list(map(lambda num: num ** 2,numbers))


result = square(3)


#Filter fonksiyonu ile liste içerisindeki elemanları filtreleyebiliriz.
def check_even(num):
    return num % 2 == 0
result= list(filter(check_even,numbers))
result = list(filter(lambda num: num % 2 == 0,numbers))

check_even = lambda num: num % 2 == 0
result = check_even(numbers[2])
print(result)

