"""Instantiating a Class!"""

"""
This is where we instantiate the 
class we defined in classes.py. 
In other words, we're creating objects 
that belong to that class.
"""

# import the class
# from <file_name>.<module_name> import <class_name>

from lessons.classes.pizza import Pizza

my_pizza: Pizza = Pizza() #CONSTRUCTOR

# accessing/setting attributes

my_pizza.size = "large"
my_pizza.toppings = 10
my_pizza.gluten_free = True