mybook={}

print("Enter the no of keys u want to enter")
n=int(input())

for i in range(0,n):
    key=input("Enter the key")
    value=input("Enter the value")

    mybook[key]=value

print(mybook)

myset = set(mybook.values())

print(myset)

for i in myset:
    print([k for k,v in mybook.items() if v == i])
