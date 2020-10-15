def split_and_join(line):
    split = line.split(" ")
    strjoin = split[0]
    for i in split[1::]:
        strjoin = strjoin + "-" + i
    return strjoin



if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)