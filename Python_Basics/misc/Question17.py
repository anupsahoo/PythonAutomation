# to print the line numbers of a particular word
n=0
word=input("Enter the word to be searched").lower()
with open("C:/Users/Rohsmiles/Desktop/Assignment.txt",'r') as f:
    for line in f:
        n+=1
        if word in line.lower():
            print(n)