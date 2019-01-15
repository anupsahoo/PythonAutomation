class magicInitCall():
    def __init__(self,animal,breed):
        self.animal=animal
        self.breed=breed

class byCall(magicInitCall):
    def __call__(self,animal,breed):
        super().__init__(animal,breed)
        print("employee method")

class byInit(magicInitCall):
    def __init__(self,animal,breed):
        super().__init__(animal,breed)

o=magicInitCall("dog","dalmasion")
ob=magicInitCall("cat","Persian")
print(o.animal)
print(ob.breed)
