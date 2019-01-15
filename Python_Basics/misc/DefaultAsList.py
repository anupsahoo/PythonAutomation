class defaultList():
    def func(self,*args, l=[]):
        l.append(args)
        print(l)

o=defaultList()
o.func('hi')
o.func('hello')
o.func('hello','ram','feed')

k=defaultList()
k.func('hi')
k.func('hello')
k.func('hello','ram','feed')
k.func()
