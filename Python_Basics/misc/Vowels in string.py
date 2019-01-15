s=input("Enter the String")
#First way to do
def fun(word):
    return word.lower() in "aeiou"
l=[i for i in filter(fun,s)]
print(l)
#Second way to do
l=['a','e','i','o','u']
[print(x) for x in s.lower() if x.lower() in l]