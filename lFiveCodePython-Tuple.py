list = [1,2,3,4,5,6,7,8,9,10]
tuple = (1,2,3,4,5,6,7,8,9,10)

print(type(list))
print(type(tuple))

print(list[2])
print(tuple[2])

print(len(list))
print(len(tuple))

list = ['Ali', 'Veli']
tuple = ('damla', 'Seda')
names = ('demet','emel')+tuple
print(names)
#TUPLEDA EKLENME DIŞARDAN YOK AMA LISTEDE VAR
list.append('Cenk')
#tuple.append('Cenk') #tuple object has no attribute 'append'


print(list)
print(tuple)
print(tuple.count('damla'))
print(tuple.index('damla'))
