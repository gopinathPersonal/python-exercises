# print common chars :you give string, strong, output should be strng
def common(word1,word2):
    a = ""
    for i in word1:
        for j in word2:
            if i==j:
                if i not in a:
                    a += i
                    break
    return a


if __name__=='__main__':
    print (common('string','strong'))