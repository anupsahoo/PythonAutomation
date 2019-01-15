file=open("./data.txt",'r')
s=file.read()
l=[i for i in s]
l.reverse()
ns=''
for i in l:
    ns+=i
print(ns)