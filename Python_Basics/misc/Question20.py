# to count the number of lines in a text file
with open("C:/Users/Rohsmiles/Desktop/Assignment.txt",'r') as f:
    n=0
    for line in f:
        n+=1
    print("Total number of lines in the file is ", n)
