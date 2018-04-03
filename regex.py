import re

# create a regex pattern –>  r=raw string, \d=a digit  .= any single character
regPhoneRegEx = re.compile(r'.\d\d\d.\d\d\d.\d\d\d\d')
myMessage = regPhoneRegEx.search("You can call me at 612 234 5678 ")
orMessage = regPhoneRegEx.search("or at (651)445-0987")
print('Phone Numbers: ' + myMessage.group())
print('Phone Numbers: ' + orMessage.group())


regPhoneRegEx = re.compile(r'.\d\d\d.\d\d\d.\d\d\d\d')
myList = (regPhoneRegEx.findall("You can call me at 612 234 5678 or at (651)345-0987"))
print ("Here is the phone number list: " , myList)

# nameString = "Albert Einstein"
# searchString = input("Enter search string:")
# print(nameString)
# T_F = re.match(".*"+searchString, nameString)
# print("T-F=: " , T_F)	# T_F boolean variable – True if found
# if T_F:				#			False if not found
#     print(T_F.group())
# else:
#     print(searchString, "not found")

print()
regPhoneRegEx = re.compile(r'.(\d\d\d)-(\d\d\d-\d\d\d\d)')
myMessage = regPhoneRegEx.search("You can call me at 612-234-5678 ")
print("You can call me at 612-234-5678 ")
print("Pattern: .(\d\d\d)-(\d\d\d-\d\d\d\d)")
print("group 1: ",myMessage.group(1))
print("group 2: ",myMessage.group(2))
print("group  : ",myMessage.group())
print("group 0: ",myMessage.group(0))
print("groups : ",myMessage.groups())
print()

heroRegEx = re.compile(r'Batman|Robin')
myHero1 = heroRegEx.search('Batman and Robin')
print(myHero1.group())
myHero2 = heroRegEx.search('Robin and Batman')
print(myHero2.group())

print(heroRegEx.findall('Robin and Batman'))


regPhoneRegEx = re.compile(r'.(\d\d\d)?-?(\d\d\d-\d\d\d\d)')
myMessage1 = regPhoneRegEx.search("You can call me at 612-234-5678 ")
print("You can call me at 612-234-5678 ")
print("Pattern: .(\d\d\d)?-?(\d\d\d-\d\d\d\d)")
print(myMessage1.group())
myMessage2 = regPhoneRegEx.search("You can call me at 234-5678 ")
print(myMessage2.group())
print()
print(ord(''))
print(chr(11))


batRegEx = re.compile(r'Bat(wo)+man')
myBat2 = batRegEx.search('Where does Batwoman live')
print("Batwoman:", myBat2.group())
myBat3 = batRegEx.search('Where does Batwowowoman live')
print("Batwowowoman:", myBat3.group())
myBat1 = batRegEx.search('Where does Batman live')
print("Batman:", myBat1)

print()
# print()
# regPhoneRegEx = re.compile(r'.[on]|[in]|[at]')
# myMessage = regPhoneRegEx.search("Jason Mraz on Aug 28, 2018 in Saint Paul, MN at Minnesota State Fair Grandstand")
#
# print(myMessage)
# print("group 0: ",myMessage.group(0))
# print("group 1: ",myMessage.group(1))
# print("group 2: ",myMessage.group(2))


print()
print()
value = "This is text [[This is translated text]]"
regex = r'((\w.*)\[\[(\w.*)\]\]|(\w.*))'
match = re.match(regex, value)
result = [x for x in match.groups() if x and x!=value]
if result:
    print(result)
else:
    print(value)

print()
print()
my_string="hello python world , i'm a beginner "
print(my_string.split("world",1)[:1])
myMessage = "Jason Mraz on Aug 28, 2018 in Saint Paul, MN at Minnesota State Fair Grandstand"
print(myMessage)
print(myMessage.split(" on ",1)[:1])
print(myMessage.split(" in ",1)[:1])
print(myMessage.split(" at ",1)[:1])
print()
print(myMessage.split(" on ",1)[1])
print(myMessage.split(" in ",1)[1])
print(myMessage.split(" at ",1)[1])
print()
print(myMessage.split(" on ",1)[1:])
print(myMessage.split(" in ",1)[1:])
print(myMessage.split(" at ",1)[1:])
print()
print(myMessage.split(" on ",1))
print(myMessage.split(" in ",1))
print(myMessage.split(" at ",1))

p0 = (myMessage.split(" on ",1))
p1 = (myMessage.split(" in ",1))
p2 = (myMessage.split(" at ",1))
print()
for num in range(2):
    print(p0[num])
print()
for num in range(len(p1)):
    print(p1[num])
print()
for num in range(len(p1)):
    print(p2[num])





print()

