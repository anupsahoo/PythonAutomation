import itertools as it
class iterCombinations():
    bills = [100, 20, 10, 5, 100]
    makes_100 = []
    for n in range(1, len(bills) + 1):
        for combination in it.combinations(bills, n):
            if sum(combination) == 100:
                makes_100.append(combination)

    print(makes_100)

o=iterCombinations()