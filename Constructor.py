class Demo:
    num=100
    def __init__(self):
        print("call constrctor")
    def demomethod(self):
        print("execute method")
d=Demo()
print(d.num)
d.demomethod()