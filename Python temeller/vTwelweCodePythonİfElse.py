if 3>3:
    print("Hoş geldiniz")


isLoggedin = True
if isLoggedin:
    print("Hoş geldiniz")


username = "admin"
password = "123456"

isLoggedin = username == "admin" and password == "123456"
if username=="admin":
    if(password == "123456"):
        print("Hoş geldiniz")
    else:
        print("password yanlış")    
else :
    print('username veya password yanlış')

x = int(input("x: "))
y = int(input("y: "))


if x > y:
    print("x y den büyük")
elif x == y:
    print("x y eşit")    
else:
    print("y x den büyük")    


num = int(input("num: "))
if num > 0:
    print("sayı pozitif",num)
elif num < 0:
    print("sayı negatif",num)
else:
    print("sayı sıfır",num)        

