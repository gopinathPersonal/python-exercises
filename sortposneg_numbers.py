import re
def numsort(num):
    num.sort()
    print(num)

numsort([2,3,4,-3,4,5,-6,-7,7,5,9])

cleanString = re.sub('[^A-Za-z]+', ' ', "Happy%$@@#*(87Christmas %%#@&NewYear")
a = list(cleanString.split())
longest = a[0]
for i in range (1,len(a)):
    if len(a[i]) > len(longest):
        longest = a[i]
    else:
        continue
print(longest)


# binary number sort keep zeros on left
bi = [0, 1, 1, 0, 0, 1, 0, 0, 1]
bi.sort()
print(bi)

def sortbin(bin_array):
    length = len(bin_array)
    ones = sum(bin_array)
    zeros = length - ones
    return [0 for _ in range(zeros)] + [1 for _ in range(ones)]

print(sortbin([0, 1, 1, 0, 0]))