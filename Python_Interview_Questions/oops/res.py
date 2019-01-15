class restrurant(object):
    bankroupt = False
    def open_branch(self):
        if not self.bankroupt:
            print("branch opened")

# Actually make a restaurant
x= restrurant()

print(x.bankroupt)

# print(restrurant().bankroupt)

