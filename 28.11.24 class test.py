class Inventory:
    def __init__(self,prodID,   prodName,prodCount):
        self.prodid=prodID
        self.prodname=prodName
        self.prodcount=prodCount
    def display(self):
        print(f"{self.prodid},{self,prodname},{self.prodcount}")
obj=Inventory(self)
obj.show()
