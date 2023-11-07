fruits = {"apple", "banana", "cherry"}
#print(fruits[0]) indesklenemez setler

for x in fruits:
    print(x)

fruits.add("orange")
print(fruits)
fruits.update(["orange", "mango", "grapes","apple"])
print(fruits)

myList = [1,1,2,2,3,3,4,4,5,5,6,6]
print(set(myList))

fruits.remove("banana")
fruits.discard("banana")
fruits.pop()
print(fruits)
fruits.clear()
print(fruits)