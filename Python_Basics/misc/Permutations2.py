import itertools as it
class iterPermutations():
    n = int(input("enter the number of elements"))
    l = []
    for i in range(n):
        a = int(input("enter digit"))
        l.append(a)
    x = list(it.permutations(l))
    for i in list(x):
        print(i)

o=iterPermutations()
