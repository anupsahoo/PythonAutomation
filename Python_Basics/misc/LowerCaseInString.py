s=input("Enter the string")
count=0

for i in s:
    if (i.islower()):
        count=count+1
print(count)