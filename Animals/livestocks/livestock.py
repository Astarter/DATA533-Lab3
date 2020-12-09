class Livestock:
    def __init__(self, owner):
        self.owner = owner

    def intoduce(self):
        print("Hi, I am %s's livestock" % self.owner)

    def display(self):
        print("Infor:")
        print("Owner: %s" % self.owner)



