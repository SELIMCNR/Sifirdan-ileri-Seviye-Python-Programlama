def changeName(n):
    n = "parametre"

name = "yiğit"
changeName(name)
print(name) #yiğit yazar value type olduğu için

def change(n):
    n[0] = "istanbul"

sehirler = ["ankara","izmir"] #referans type olduğu için değişir değeri.
n = sehirler[:] #copy
n[0] = "istanbul"
print(sehirler)
print(n)
change(sehirler)

def add(a,b,c=0,d=0,e=0):
    return sum((a,b))

print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,40))

def add(*params): #*params çoklu parametre alır. tuple olarak alır.
    print(type(params))
    print(params)
    print(params[0])
    return sum((params))
print(add(10,20,30,40,50,60))


def add(*params):
    sum = 0
    for n in params:
        sum = sum + n
    return sum
print(add(10,20,30,40,50,60))

def displayUser(**args): #**args çoklu parametre alır. dictionary olarak alır.
    print(type(args))
    for key,value in args.items():
        print("{} is {}".format(key,value))

displayUser(name = "Çınar", age = 2, city = "istanbul")
displayUser(name='Yiğit',age=14,city='ankara',phone='123456')

def myfunction (a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
myfunction(10,2,3,4,5,key1 = "value1",key2 = "value2")
