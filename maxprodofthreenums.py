def maxprod(num):
    num.sort()
    print(num)
    print(num[-1], num[-2], num[-3])
    print(num[-1], num[0], num[1])
    return( max(num[-1] *num[-2] *num[-3], num[-1] *num[0] *num[1]))

print(maxprod([2,3,4,-3,4,5,-6,-7,7,5,9]))