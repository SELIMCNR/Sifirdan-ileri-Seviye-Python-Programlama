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


