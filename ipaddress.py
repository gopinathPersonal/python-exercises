def defangIPaddr(add):
    newaddr =""
    for i in add:
        if(i == "."):
            newaddr = newaddr + "[.]"
        else:
            newaddr = newaddr + i
    return newaddr

address = "255.100.50.0"
result = defangIPaddr(address)
print(result)