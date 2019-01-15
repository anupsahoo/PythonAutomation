
try:
    l = [15, 25, 35]
    i = iter(l)
    print (next(i))
    print (next(i))
    print (next(i))
    print (next(i))
except Exception as e:
    print (type(e))