# progam to find max consequtive 1s in an array of 0's and 1s

num = list(input("enter the binary number"))
count = 0
max = 0

for i in num:
    if i == '1':
        count += 1
        if count > max:
            max = count
    elif i == '0':
        count = 0
print(max)



