name = 'Selim'
surname = 'Çınar'
age = 36
message = 'My name is '
greeting = message+name+' '+surname+' and \n I am '+str(age)+' years old.'
length = len(greeting)

print(greeting)
print(greeting[0])
print(greeting[3])
print(greeting[length-1])
print(greeting[-1])
print(greeting[4:9])
print(greeting[4:])
print(greeting[:25])
print(greeting[2:30:2])


Soru1 = 'lorem ipsum is dummy text'
Soru2 = 'lorem ipsum is not dummy text'
Soru3 = 'lorem ipsum is dummy text lorem ipsum is dummy text lorem ipsum is dummy text'

Sorular = Soru1 + Soru2 + Soru3 
length = len(Sorular)
print(Sorular)
print(Sorular[0:100])
print(Sorular[0:5])
print(Sorular[0:2:18])
print(Sorular[0:3:21])
print(Sorular[length-1])
print(Sorular[0:20])



cümle = 'Lorem ipsum dolor sit amet consectetur adipisicing elit.'
print(cümle)
print(cümle[0])
print(cümle[0:2:20])
print(cümle[-5])

sentence = 'My name is Selim Çınar and \n I am 23 years old.'
school = 'I am studying at university in Turkey Kahramanmaraş Sütçü İmam University'
section = 'Bilgisayar programcılığı'
class1 = 'Graduate.'
print(sentence +" "+ school +" "+ section+" "+ class1)
      