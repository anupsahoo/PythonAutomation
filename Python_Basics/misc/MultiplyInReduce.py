import functools
class MultiplyElementsInList:
    def multiplyElements(self):
        l = [10, 5, 4, 2]
        op=functools.reduce(lambda a,b:a*b,l)
        print(op)

ob=MultiplyElementsInList()
ob.multiplyElements()