try:
    f=open("rohith.txt",'r')
    f.write("Hi")
except Exception as e:
    print(type(e))