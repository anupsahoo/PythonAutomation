l = [21,25,30,48,41]
l2=reversed(l)
l1 = list(map(lambda x,y:x*y,l,l2))
print(l1)
