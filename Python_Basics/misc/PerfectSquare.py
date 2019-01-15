import math
def isPerfectSquare(n):
    s=math.sqrt(n)
    return ((s-math.floor(s))==0)
for i in range(100):
    if isPerfectSquare(i):
        print(i," Its a perfect square")
    else:
        print(i, " Its not a perfect square")