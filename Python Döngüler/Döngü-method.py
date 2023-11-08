list = [1,2,3]

for item in list:
    print(item)

for item in range(50,100,20):
    print(item)

print(list(range(50,100,10)))


#enumarete

index = 0
greeting = 'Hello There'
for letter in greeting:
    print(letter)
    index +=1        

for index,letter in enumerate(greeting):
    print(f"index : {index} letter : {letter}")


#zip
list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
list3 = [100,200,300,400,500]
print(list(zip(list1,list2,list3)))   

for a,b,c in zip(list1,list2,list3):
    print(a,b,c)




