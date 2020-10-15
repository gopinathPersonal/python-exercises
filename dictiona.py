if __name__ == '__main__':
    mydict={}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        mydict[name] = score

    mylist = sorted(mydict.values())
    g = mylist[1]
    final =[]
    for name, score in mydict.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
        if score == g:
            final.append(name)
    print(sorted(final))