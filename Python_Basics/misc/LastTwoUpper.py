s=input("Enter the string")
wrd=s.split()
count=0
for i in wrd:
    print(i.upper())
    count+=1
    if count>1:
        break