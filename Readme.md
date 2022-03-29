# Python OOPs

[Object Oriented Programming with Python - Full Course for Beginners](https://youtu.be/Ej_02ICOIgs)

Object → Instance of a class

Methods → Function Inside a class  ( Instance Method, Class Methods and Static Methods)

Attributes → Variables inside class

- Class Level Attributes
- Instance Level Attributes

## Constructor

```python
#Example for python constructor
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
```

## Magic Attributes

[Explore the Magic Methods in Python - Analytics Vidhya](https://www.analyticsvidhya.com/blog/2021/08/explore-the-magic-methods-in-python/)

- `__dict__` : Show all class attributes
- `__repr__` : Can be used to Modify the representation of the object
- `__init__` : Constructor of a class.

## Static and Class Methods

### **Class Method :**

Class method are methods bound to the class and not the objects of the class. They can be accessed by all the objects of the class.

### **Static Method :**

Static methods in Python are extremely similar to python class level methods, the difference being that a static method is bound to a class rather than the objects for that class.

This means that a static method can be called without an object for that class. This also means that static methods cannot modify the state of an object as they are not bound to.

### Class method vs Static Method

- A class method takes `cls` as the first parameter while a static method needs no specific parameters.
- A class method can access or modify the class state while a static method can’t access or modify it.
- In general, static methods know nothing about the class state. They are utility-type methods that take some parameters and work upon those parameters. On the other hand class methods must have class as a parameter.
- We use `@classmethod` decorator in python to create a class method and we use `@staticmethod` decorator to create a static method in python.

- **Code Example**
    
    ```python
    # When to use class methods and when to use static methods ?
    
    class Item:
        @staticmethod
        def is_integer():
            '''
            This should do something that has a relationship
            with the class, but not something that must be unique
            per instance!
            '''
        @classmethod
        def instantiate_from_something(cls):
            '''
            This should also do something that has a relationship
            with the class, but usually, those are used to
            manipulate different structures of data to instantiate
            objects, like we have done with CSV.
            '''
    
    # THE ONLY DIFFERENCE BETWEEN THOSE:
    # Static methods are not passing the object reference as the first argument in the background!
    
    # NOTE: However, those could be also called from instances.
    
    item1 = Item()
    item1.is_integer()
    item1.instantiate_from_something()
    ```
    

## Object Oriented Programming Principles

1. Inheritance
2. Encapsulation
3. Polymorphism 
4. Abstraction

### Inheritance

## Notes

- Python passes object itself as first argument for all the class methods.
- Static Methods inside class work the same way as normal function.