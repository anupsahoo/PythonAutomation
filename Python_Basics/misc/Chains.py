import itertools as it

class iterChains():
    l1 = [1, 4, 3]
    l2 = [5, 2, 7]

    l = sorted([i for i in it.chain(l1, l2)])
    print(l)