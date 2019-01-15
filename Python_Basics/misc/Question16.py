# to append the contents of one file into another file
with open("./data.txt",'r') as f:
    s=f.read()
with open("./data1.txt",'w') as f1:
    f1.write(s)
