# program to print 1, 121, 12321, 1234321,

num = int(input("enter the number: "))
str1 = ""
'''
for i in range(1,num+1):
    print(int((10**i-1)/9)**2)
'''

for i in range(1,num+1):
    str1 = str1 + str(i)
    #str2 = str1+ str1[i+1::-1]
print(str1[0:len(str1)-1] + str1[::-1])

# binary to


