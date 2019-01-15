# def sum_num(n1,n2):
#     print(n1+n2)
# sum_num(2,3)

# return statement
# def sum_num(n1,n2):
#     """
#     this method is for sum of two numbers
#     :param n1:
#     :param n2:
#     :return:
#     """
#     return n1+n2
# sum_num(2,3)
#
# def isMetro(city):
#     l = ['blr', 'hyd', 'mum']
#     if city in l:
#         return True
#     else:
#         return False
# x = isMetro('blr')
# print(x)

# optional Parameter

# def sum_num(n1= 3,n2= 5):
#     """
#     this method is for sum of two numbers
#     :param n1:
#     :param n2:
#     :return:
#     """
#     return n1+n2
# x = sum_num(2,3)
# print(x)
# y =sum_num()
# print(y)


a = 10
def test_method(a):
    print("value of a is :" +str(a))
    a= 2
    print("value of a is: "+str(a))
x = test_method(a)
print("value of a is: "+str(a))

# define Global value

def test_method():
    global a
    print("value of a is :" +str(a))
    a= 2
    print("value of a is: "+str(a))
x = test_method()
print("value of a is: "+str(a))