class magicMul():
    def mul(self, a, b):
        return a.__mul__(b)

o=magicMul()
print(o.mul(10,200))
