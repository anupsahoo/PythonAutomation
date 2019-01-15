s="Somari Siddha"
l=[x.upper() if x.islower() else x for x in s]
[print(i, end='') for i in l]