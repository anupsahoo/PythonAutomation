n=int(input("enter the number of words to be add"))
l=[]
for i in range(n):
    l.append(input("enter the word"))

l1=[len(i) for i in l]
print("Length of the longest word is ",max(l1))
