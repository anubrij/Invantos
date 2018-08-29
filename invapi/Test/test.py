class Test(object):
    """docstring for Test."""
    def __init__(self, *arg):
        self.value = arg[0]
        pass
    def CallHi(self):
        print(self.value)

x = Test("anubrij")
x.CallHi()
Test.CallHi(x)
