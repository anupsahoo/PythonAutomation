class Odd:

    def __next__(self,num):
        self.num=num
        self.num += 2
        if self.num%2==1:
            return self.num

obj=Odd()
for i in range(3):
    print(obj.__next__(i))
