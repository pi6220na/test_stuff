mylist = []

mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)
mylist.append(5)
mylist.append(6)

for item in mylist:
    print(item)

print(mylist)

newitem = mylist.pop(0)
print(newitem)
print(mylist)
print()

myDict = {}
x = 0
for x in range(0,6):
    myDict[x] = x + 11
    print(myDict.items())

print(myDict)
print()

try:
    print(myDict.items())
except:
    print('dictionary error')

for j in myDict:
    print(myDict[j])

print(type(myDict))
print(myDict.keys())
print(myDict.items())
print(myDict.values())
print(myDict)