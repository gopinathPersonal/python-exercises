# progaram to find largest product of two consequetive

class Product2():
    def prod(self, n):
        if len(n) != 0:
            largest = n[0] * n[1]
            for i in range(1, len(n)-1):
                if n[i] * n[i+1] > largest:
                    largest = n[i] * n[i+1]
                else:
                    continue
            return largest




p = Product2()
print(p.prod([2,3,1,4,3,7,2,9,1]))