# to find the largest number in a list
# first way
l=[21,64,55,23,48,57]
print(max(l))
# second way
print(sorted(l)[-1])
# third way
l1=[i for i in sorted(l)]
l1.reverse()
print(l1[0])