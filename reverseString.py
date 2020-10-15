

def reverseString(strorg):
    length = len(strorg)
    strreversed = ""
    finalrevSen =""
    for i in strorg[::-1]:
        strreversed += i
    return strreversed


sen = input(" enter the sentence: ")
li = sen.split()
newSen = " "
for i in range(len(li)):
    newSen = newSen + " " +reverseString(li[i])
print(newSen)