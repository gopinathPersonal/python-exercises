def secondLargest(array):
    mylist = sorted(set(array))
    print(mylist)
    print(mylist.pop(-2))

array = [12, 35, 1, 10, 34, 1, 35]
secondLargest(array)