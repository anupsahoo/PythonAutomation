#Capitalize Every word of a file
file=open("./data.txt",'r')
s=file.read()
ls=s.split(' ')
[print(i.capitalize(),end=' ') for i in ls]