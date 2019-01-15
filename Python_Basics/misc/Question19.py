# to read a text file and print all the numbers present in text file
with open("C:/Users/Rohsmiles/Desktop/Assignment.txt",'r') as f:
    s=f.read()
    l=[i for i in s]
    l1=[]
    [l1.append(x) for x in l if x.isdigit()]
    print(l1)