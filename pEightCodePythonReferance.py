#Value types değerle 
x = 5
y = 25

x = y
y = 10

print(x,y)

#Reference types adresle 
a = ["apple", "banana"]
b = ["apple", "banana"]

a = b
b[0] = "grape"
print(a,b)