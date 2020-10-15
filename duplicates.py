
mystring = input("enter the string: ")
length = len(mystring)
dupli =[]
for i in mystring:
    if(mystring.find(i) == 1):
        dupli.append(i)
duplic = sorted(set(dupli))
nodupli = sorted(set(mystring))
print(nodupli)
print(duplic)


li = list(input("enter numbers to remove duplicates: "))
length = len(li)
x = set()
for i in li:
    x.add(i)
print(list(sorted(x)))