from item import Item

item1 = Item('Phone',100,1)
print(item1.pay_rate)

item1.pay_rate = 0.9 
print(item1.pay_rate)

item1.cat = 0.7
print(item1.cat)


del item1

print(Item.all)