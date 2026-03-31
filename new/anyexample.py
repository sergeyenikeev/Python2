s = "Abcdefg"
for i in s:
    print(i)

for i, ii in enumerate(s):
    print(i, ii)

class MyRange():
    def __init__(self, n):
        self.n = n
        self.i = 0
    def __iter__(self):
        return self 
    def __next__(self):
        # while (self.i <= self.n):
        #     self.i += 1
        #     yield self.i
        #     raise StopIteration
            
        self.i += 1
        if self.i <= self.n:
            return self.i
        raise StopIteration

for i in MyRange(5):
    print(i)

for i in MyRange(5):
    print(i)

def mygen2(n):
    for i in range(n):
        yield i

for i in mygen2(3):
    print(i)