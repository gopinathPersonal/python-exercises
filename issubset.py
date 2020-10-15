def isSubsect(s, p):
    length = len(p)
    issect = False
    for i in range(length):
        for j in range(len(s)):
            if p[i] == s[j]:
                issect = True
                break
            else:
                issect = False
    return issect
m = ['a','b','c','d']
#m = [1, 5, 4, 6, 8 , 2]
#n= [5, 8, 2, 7]
n = ['a','e']
output = isSubsect(m, n)
print(output)