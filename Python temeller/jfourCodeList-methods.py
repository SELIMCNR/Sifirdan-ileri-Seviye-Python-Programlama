numbers = [1,10,5,16,4,9,10]
letters = ["a","g","s","b","y","a","s"]

val = min(numbers)
val = max(numbers)
val = min(letters)
val = max(letters)

val = numbers[3:6]
val = numbers[:3]
val = numbers[4:]
#ekleme
numbers[4] = 40
numbers.append(49)
numbers.append(49)

numbers.insert(3,78)
numbers.insert(-1,52)
#silme
numbers.pop()
numbers.remove(1)
numbers.sort()
#sıralama
numbers.sort()
numbers.reverse()

letters.sort()
letters.reverse()

print(val)


print(len(numbers))
print(len(letters))

print(numbers.count(10))
print(letters.count("a"))

numbers.clear()
print(numbers)

UserA = ["User"]
if UserA[0] =="User":
    UserA.append("Admin")
    UserA.insert(0,"SuperAdmin")
    UserA.pop()
    UserA.sort()
    print(UserA)

UserScore = [70,80,90,100]
UserScore.sort()
print(max(UserScore))
print(min(UserScore))
print(UserScore.count(70))    