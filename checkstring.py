def checkstring(article, ransom):
    a = list(ransom.split())
    b = list(article.split())
    found = False
    for item in a:
        for word in b:
            if(item == word):
                found = True
                break
            else:
                found = False
        if(found == False):
            break

    return found

article = input("enter string for article: ")
ransom = input("enter string for ransom: ")
result = checkstring(article, ransom)
print(result)