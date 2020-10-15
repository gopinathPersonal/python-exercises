num  = list(input("Enter the list of numbers : "))
print(sorted(set(num)))

mystr = input("enter the string: ")
revstr = ""
for i in mystr[::-1]:
    revstr = revstr + i

print(revstr.lower())