def checkstring(article):
    newstr = ""
    for item in article:
        if(item not in('a', 'e', 'i', 'o', 'u')):
            newstr = newstr + item
        else:
            newstr = newstr

    return newstr

article = input("enter string for article: ")
result = checkstring(article)
print(result)