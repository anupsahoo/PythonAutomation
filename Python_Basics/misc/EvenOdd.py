l=[1,2,1,3,4,5,6,7,8,12,45,66,58,41]
l1=list(filter(lambda l:l%2==0,l))
l2=list(filter(lambda l:l%2!=0,l))
print("Even List : " ,l1,"\n","Odd List : ",l2)