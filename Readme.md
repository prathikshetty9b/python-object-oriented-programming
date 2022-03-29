# Python Object Oriented Programming

### Reference : [Object Oriented Programming with Python](https://youtu.be/Ej_02ICOIgs)

Object → Instance of a class

Methods → Function Inside a class  ( Instance Method, Class Methods and Static Methods)

Attributes → Variables inside class

- Class Level Attributes
- Instance Level Attributes

## Class `item.py`

```python
import csv

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @property
    def name(self):
        # Property Decorator = Read-Only Attribute
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.__price * self.quantity

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"
```

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
    

## Getters and Setters

[Getter and Setter in Python - GeeksforGeeks](https://www.geeksforgeeks.org/getter-and-setter-in-python/)

In Python, getters and setters are not the same as those in other object-oriented programming languages. Basically, the main purpose of using getters and setters in object-oriented programs is to ensure data encapsulation. **[Private variables in python](https://www.geeksforgeeks.org/private-variables-python/)** are not actually hidden fields like in other object oriented languages. Getters and Setters in python are often used when:

- We use getters & setters to add validation logic around getting and setting a value.
- To avoid direct access of a class field i.e. private variables cannot be accessed directly or modified by external user.

### Code Example

```python
	  #Getter
    @property
    # Property Decorator = Read-Only Attribute
    def name(self):
        return self.__name

    #Setter
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value
```

## Object Oriented Programming Principles

1. Inheritance
2. Encapsulation
3. Polymorphism 
4. Abstraction

## Inheritance

[Types of inheritance Python - GeeksforGeeks](https://www.geeksforgeeks.org/types-of-inheritance-python/)

**Inheritance ****allows us to define a class that **inherits** all the methods and properties from another class.

### **Types of Inheritance in Python Programming**

1. Single inheritance
2. Multiple inheritances
3. Multilevel inheritance
4. Hierarchical inheritance
5. Hybrid inheritance

### Code Example

```python
from item import Item

#New phone class inherited from Item class
class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, broken_phones = 0):
        super().__init__(name, price, quantity)

        #Run validiation for recieved arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than or equal to zero"

        #Assign to self object
        self.broken_phones = broken_phones
```

## Encapsulation

[](https://pynative.com/python-encapsulation/#:~:text=Encapsulation%20in%20Python%20describes%20the,methods%20into%20a%20single%20unit)

Encapsulation in Python describes the concept of **bundling data and [methods](https://pynative.com/python-instance-methods/) within a single unit.** So, for example, when you create a [class](https://pynative.com/python-classes-and-objects/), it means you are implementing encapsulation. A class is an example of encapsulation as it binds all the data members ([instance variables](https://pynative.com/python-instance-variables/)) and methods into a single unit.

Example : Class

### **Advantages of Encapsulation**

- **Security**: The main advantage of using encapsulation is the security of the data. Encapsulation protects an object from unauthorized access. It allows private and protected access levels to prevent accidental data modification.
- **Data Hiding**: The user would not be knowing what is going on behind the scene. They would only be knowing that to modify a data member, call the setter method. To read a data member, call the getter method. What these setter and getter methods are doing is hidden from them.
- **Simplicity**: It simplifies the maintenance of the application by keeping classes separated and preventing them from tightly coupling with each other.
- **Aesthetics**: Bundling data and methods within a class makes code more readable and maintainable

## Abstraction

[Understanding Abstraction in Python - AskPython](https://www.askpython.com/python/oops/abstraction-in-python)

**Abstraction** focuses on hiding the internal implementations of a process or method from the user. In this way, the user knows what he is doing but not how the work is being done.

## Polymorphism

[Polymorphism in Python](https://www.programiz.com/python-programming/polymorphism)

The literal meaning of polymorphism is the condition of occurrence in different forms.

Polymorphism is a very important concept in programming. It refers to the use of a single type entity (method, operator or object) to represent different types in different scenarios.

### Function Polymorphism in Python

There are some functions in Python which are compatible to run with multiple data types.

One such function is the `len()` function. It can run with many data types in Python. Let's look at some example use cases of the function.

### **Example 2: Polymorphic len() function**

```python
print(len("Programiz"))
print(len(["Python", "Java", "C"]))
print(len({"Name": "John", "Address": "Nepal"}))
```

**Output**

```

9
3
2
```

## Notes

- Python passes object itself as first argument for all the class methods.
- Static Methods inside class work the same way as normal function.
- `super()` → Is used to access attributes and methods from parent class
