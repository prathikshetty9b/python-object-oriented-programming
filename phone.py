from item import Item

#New phone class inherited from Item class
class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, broken_phones = 0):
        super().__init__(name, price, quantity)

        #Run validiation for recieved arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than or equal to zero"

        #Assign to self object
        self.broken_phones = broken_phones
    


