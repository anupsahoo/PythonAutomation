l=[1,2,5,1,6,2,4,1,2]
l2=[]
[l2.append(i) for i in l if i not in l2]
print(l2)