class stack:

    def __init__(self):

        self.array = []
        self.top = -1
        self.max = 100

    def isEmpty(self):

        if self.top == -1:
            return True
        else:
            return False
    def isFull(self):
        
        if self.top == self.max - 1:
            return True
        else:
            return False

    def push(self, data):

        if self.isFull():
            print('Stack OverFlow')
            return
        else:
            self.top += 1
            self.array.append(data)	

    def pop(self):

        if self.isEmpty():
            print('Stack UnderFlow')
            return
        else:
            self.top -= 1
            return self.array.pop()

class SpecialStack(stack):

    def __init__(self):
        super().__init__()
        self.Min = stack()

    def push(self, x):

        if self.isEmpty():
            super().push(x)
            self.Min.push(x)
        else:
            super().push(x)
            y = self.Min.pop()
            self.Min.push(y)
            if x <= y:
                self.Min.push(x)
            else:
                self.Min.push(y)

    def pop(self):

        x = super().pop()
        self.Min.pop()
        return x

    def getmin(self):

        x = self.Min.pop()
        self.Min.push(x)
        return x

# Driver code
if __name__ == '__main__':

    s = SpecialStack()
    print ("Enter the number of elements\n")
    n=int(input())
    data=[int(x) for x in range(n)]

    for i in data:
        s.push()
        
    print(s.getmin())
    s.push(5)
    print(s.getmin())

