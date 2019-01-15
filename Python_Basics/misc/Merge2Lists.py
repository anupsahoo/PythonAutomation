import itertools
l=[1,2,3,4,2,5]
l1=[55,20,78,60,35]
print(sorted([x for x in itertools.chain(l, l1)]))
