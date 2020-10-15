mylist1 = [3,1,0,6,7,5]
mylist2 = mylist1[:]  # creates new copy of lsit
mylist3 = mylist1.copy() # creates new copy of list

# sort and sorted
mylist2.sort()
print(mylist2)
print(sorted(mylist3))
mylist1.sort()
print(mylist1)
