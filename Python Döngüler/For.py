# list of döngüler
numbers=[1,2,3,4,5]

for number in numbers:
    print(number)


names = ['ç','s','s']

for name in names:
    print(f'my name is {name}')

#tuple of döngüler
tuple = [(1,2),(1,3),(3,5)]

for t,s in tuple:
    print(t,s)

#dictionary of döngüler
d = {'k1':1,'k2':2,'k3':3}

for item in d :
    print(item)

for item,value in d.items():
    print(item,value)    


scores = [10,20,30,40,50,60,70,80,90,100]
toplamscore = 0
for score in scores:
    toplamscore+=score
print(toplamscore)
    
