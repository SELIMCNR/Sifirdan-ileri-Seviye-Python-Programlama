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


#Boy hesabı karşılaştırması
boy = float(input("Boyunuz :   örnek(1.80)"))
if boy>1.90 and boy<2.10:
    print(f"Boyunuz bu  {boy} ve uzunsunuz ") 
elif boy>1.70 and boy <1.90:
    print(f"Boyunuz bu {boy} ve ortalama uzunluktasınız") 
elif boy>1.50 and boy <1.70:
    print(f"Boyunuz bu {boy} ve kısa boylusunuz")       
