def runnerup(num):
    n = len(num)
    temp = 0

    for i in range(0,n):
        for j in range(i+1, n):
            if num[i] < num[j]:
                temp = num[i]
                num[i] = num[j]
                num[j] = temp
    return

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    runnerup(arr)
for i in  range(0,n):
    print(arr[i],end=" " )
print(arr[1])

