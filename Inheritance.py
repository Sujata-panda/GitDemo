from VariableDemo import Demo   # from file import class name


class DemoInheritance(Demo):    # here inherit Demo class
    num2 = 100

    def __init__(self):
        Demo.__init__(self, 2, 3)  # calling demo class constructor

    def getcompletedata(self):
        return self.num2 + self.num + self.summation()  # num and summation is Demo class variable call direclty without create object


obj = DemoInheritance()
obj.getcompletedata()