x = "global x" # global scope
def function():
    x = "local x" # local scope
    
function()
print(x)    

name = "Çınar"
def changeName(new_name):
    name = new_name
    print(name)
changeName("Asım")
print(name)    

## global local scope ##
name = "global string"
def greeting():
    name = "Çınar"
    
    def hello():
        print("Hello "+name)
    hello()
greeting()    

x = 50
def test(x):
    
    print(f"x: {x}")

    x = 100
    print(f"changed x to {x}")
test(x)
print(x)    
