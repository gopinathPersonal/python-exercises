mystring = input("enter the String: ")

length = len(mystring)
newStr = ""
if (length % 2 == 0):
    half = length // 2
    a = mystring[0:half]
    newStr = str(a) + str(a)[::-1]

else:
    half = (length // 2) + 1
    a = mystring[:half]
    newStr = str(a)[0:half-1] + str(a)[::-1]

#print(mystring, newStr)

if(mystring == newStr):
    print('String is a polyndrome')
else:
    print('String is Not a polyndrome')
