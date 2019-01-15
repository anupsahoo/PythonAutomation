class Onida():
    def display(self):
        print("from onida television")

class LG():
    def display(self):
        print("from LG television")

class View(Onida,LG):
    print("Watching", end=' ')


ob=View()
ob.display()
