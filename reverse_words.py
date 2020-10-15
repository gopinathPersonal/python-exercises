def rev_string(s):
    str = ''
    ans = ''
    for i in s:
        if i != ' ':
            str = str + i
        else:
            ans = str + ' ' + ans
            str = ''
    ans = str + ' ' + ans
    print(ans)

str= "Welcome to the World"
rev_string(str)


