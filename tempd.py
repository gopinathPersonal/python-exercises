str1 = "aabbbccddddaabbbcdefwdddaaabb"
let = str1[0]
newstr = ""
count = 0
for i in str1:
    if(let == i):
        newstr = newstr + i
        let = i
        count = count + 1
    else:
        newstr = newstr + str(count)
        let = i
        count = 0
        newstr = newstr + i
        count = count + 1

newstr = newstr + str(count)
print(newstr)