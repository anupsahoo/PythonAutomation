# we can iterate over a string , list, touple, dict items using for loop
#
# my_string= "Hello"
# for x in my_string:
#     print(x, end=' , ')


# my_string = "Hello"
# for x in my_string:
#     if x == "H":
#         print("h", end =' ,')
#     else:
#         print(x, end=' , ')
#
# cars = ['maruti', 'audi', 'honda']
# for car in cars:
#     print(car, end= " , ")
#
# num = [1,2,3]
# for n in num:
#     print(num*10)

# d = {'one': 1 , 'two': 2, 'three': 3}
# for k in d:
#     print(k)
# d = {'one': 1 , 'two': 2, 'three': 3}
# for k,v in d.items():
#     print(k)
#     print(v)

# zip function
# l1= [1,2,3]
# l2 = [6,7,8,9]
# for a,b in zip(l1,l2):
#     print(a)
#     print(b)

# range function- helps to create sequence of numbers and does not save them in memory

print(list(range(0,10)))

a = range(10,20)
print(list(a))

for num in range(4):
    print(num)

