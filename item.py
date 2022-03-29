# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=trailing-whitespace


import csv

class Item : 
    pay_rate = 0.8 # Discount of 20%
    all = [] #empty list to contain  all Item objects 
    def __init__(self,name : str,price : float,quantity : int):
        #Run Validation to recieved arguments
        assert price >= 0, f"Price {price} is not greater or equal to 0"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to 0"

        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        #Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return (self.price * self.quantity)
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as file:
            reader = csv.DictReader(file)
            items = list(reader)
        
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity= float(item.get('quantity'))
            )
  
    @staticmethod
    def is_integer(num):
        if isinstance(num,float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False

    def __repr__(self):
        #Represent object in a more readable manner
        return f"Item({self.name},{self.price},{self.pay_rate},{self.quantity})\n"

    
