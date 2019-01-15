class Construct():
    def __init__(self):
        print("from Constructor")

    def __del__(self):
        print("from destructor")

ob=Construct()
del ob