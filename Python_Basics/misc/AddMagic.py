class magicAdd():
    def sum(self,a, b):
        return a.__add__(b)


o=magicAdd()
print(o.sum("hello ", "hi"))
