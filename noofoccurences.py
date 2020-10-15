

def noofoccur(s):
    length = len(s)
    mydict = {}

    for char in s:
        if char in mydict:
            mydict[char] += 1
        else:
            mydict[char] = 1
    return mydict
#m = ['a','b','c','d']
#m = [1, 1, 4, 6, 2 , 2]

m = "this"
#n= [5, 8, 2, 7]
#n = ['a','i']
output = noofoccur(m)
print(output)
