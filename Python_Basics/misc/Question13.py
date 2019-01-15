# Program for fibonaci series
a,b=0,1
for i in range(6):
    a,b=b,(a+b)
    print(b,end=' ')