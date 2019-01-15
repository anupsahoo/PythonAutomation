s1=input("Enter the first string:")
s2=input("Enter the Second string:")
s3 = set(set(s1) & set(s2))
if len(s3)>0:
    print("Common letters present in two input strings")
print(s3)