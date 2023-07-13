'''
• Create a class Tree
• Let instances of class Tree have leaves
• Let there be a function set_season
• If the season is Winter or Autumn Trees should not have leaves
##Exceptions
Many languages have the concept of the “Try-Catch” block. Python uses four keywords: try, except, else, and finally. 
Code that can possibly throw an exception goes in the try block. except getsthe code that runs if an exception is raised. 
Else is an optional block that runs if no exception was raised in the try block, 
and finally is an optional block of code that will run last, regardless of if an exception was raised. 
We will focus on try and except for this chapter. 

A basic example looks like this:

```
#An except clause may have multiple exceptions,
#given as a parenthesized tuple:
try:
    # Code to try
    
except (RuntimeError, TypeError, NameError):
    # Code to run if one of these exceptions is hit

try:
    # Code to try

except RuntimeError:
    # Code to run if there's a RuntimeError

except TypeError:
    # Code to run if there's a TypeError

except NameError:
    # Code to run if there's a NameError

#Finally, we have finally. finally is an optional block that
#runs after try, except, and else, regardless of if an exception
#is thrown or not. This is good for doing any cleanup that you
#want to happen, whether or not an exception is thrown.

try:
    raise KeyboardInterrupt
    
finally:
    print("Goodbye!")
```
'''

class Tree:
    def __init__(self):
        self.leaves = []

    def set_season(self, season):
        if season == "Winter" or season == "Autumn":
            self.leaves = []
        else:
            raise ValueError("Invalid season!")

my_tree = Tree()

# Setting the season to Winter
my_tree.set_season("Winter")
print("Leaves in Winter:", my_tree.leaves)

# Setting the season to Summer
try:
    my_tree.set_season("Summer")
    print("Leaves in Summer:", my_tree.leaves)
except ValueError as e:
    print("Leaves in Summer:", e)
