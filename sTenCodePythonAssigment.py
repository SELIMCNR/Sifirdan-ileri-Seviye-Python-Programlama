x , y,z = 5,10,20

x = x+5
x +=5 
print(x,y,z)

x +=5
x -=5
x *=5
x /=5
x %=5
x //=5
y **=z

print(x,y,z)

values = 1,2,3,4,5,6
print(values)
print(type(values))

x,y,*z = values
print(x,y,z[2])




x,y,z = 2,5,10
numbers = 1,5,7,10,6
# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir ?
a = int(input("1.sayı: "))
b = int(input("2.sayı: "))
result = (a*b)-(x+y+z)
print(result)

# 2- y'nin x'e kalansız bölümünü hesaplayınız.
result = y//x
# 3- (x,y,z) toplamının mod 3'ü nedir ?
result = (x+y+z)%3
# 4- y'nin x. kuvvetini hesaplayınız.
result = y**x

# 5- x, *y, z = numbers işlemine göre z'nin küpü kaçtır ?
result = z**3
# 6- x, *y, z = numbers işlemine göre y'nin değerleri toplamı kaçtır ?
result = y[0]+y[1]+y[2]