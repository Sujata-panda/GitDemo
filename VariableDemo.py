class Demo:
    num = 100#class variable

    def __init__(self, a, b):
        self. firstvariable = a #instance variable
        self.secondvariable = b #instance variable
        print("call constrctor")

    def demomethod(self):
        print("execute method")

    def summation(self):
        return self.firstvariable + self.secondvariable + self.num + Demo.num + d.num


d = Demo(2, 3) #object ceation
print(d.num) #calling class variable self.num, Demo.num ,d.num
print(d.summation()) #calling method

d1 = Demo(3, 4)
print(d1.num)
print(d.summation())

