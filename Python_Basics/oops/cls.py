class human(object):

    age = 30
    def __init__(self, hight, weight):
        self.my_hight = hight
        self.my_weight = weight
        print("class level object initialization")

    def eat(self):
        print("this is a eat action")

    def sleep(self):
        print("this is sleep action")

    def repeat(self):
        print(" eat - sleep - repeat")

class salmankhan(human):

    def __init__(self):
        human.__init__(self, 15, 30)
        print("Salman Khan Object created and inheritated from human class")

    def sleep(self):
        super().sleep()
        print("I sleep while driving")

# anup = human(20,50)
# print(anup.my_hight)
# print(anup.my_weight)
# print(anup.age)
# anup.age = 42
# print(anup.age)
# anup.sleep()
# anup.eat()
# anup.repeat()

s = salmankhan()
print(s)
s.sleep()