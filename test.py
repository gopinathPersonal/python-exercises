def myfun(mystring):
	newstr = ""
	for i in mystring:
		if i.isupper():
			newstr = newstr + i.lower()
		else:
			newstr = newstr + i
	return newstr

result = myfun("Hello GoPi")
print(result)

