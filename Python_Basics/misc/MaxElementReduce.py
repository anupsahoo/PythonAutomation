import functools
class MaxElementInList:
    def maxElementInList(self):
        l = [10, 50, 40, 32]
        op=functools.reduce(lambda a,b:a if a>b else b,l)
        print(op)

ob=MaxElementInList()
ob.maxElementInList()