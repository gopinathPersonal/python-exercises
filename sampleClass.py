class ops:
    def add(self, a, b):
        return (a + b)
    def subt(self, a, b):
        return (a - b)
    def multi(self, a, b):
        return (a * b)
    def divs(self, a, b):
        return (a / b)
    def mod(self, a, b):
        return (a % b)

a = ops()
print("Addition", a.add(5, 2))
print("Subtraction", a.subt(5, 2))
print("Mutliplication", a.multi(5, 2))
print("Division", a.divs(5, 2))
print("type of divistion", type(a.divs(5, 2)))
print("Modular", a.mod(5, 2))
