
'''
#% -> Python by default doesn't support abstract classes
#% -> Abstract class can't be instantiated
#% -> Abstract class can have abstract methods with no body
#% -> Abstract class can have abstract properties

#? References : https://www.geeksforgeeks.org/abstract-classes-in-python/
'''

# Imports
from abc import ABC,abstractclassmethod

class Abstract1(ABC):
    
    @abstractclassmethod    #? This decorator maked this display method abstract
    def display(self):
        print("Abstract display method")

class ImplAbstract1():
    
    def display(self):
        print("Override display method")
    
try:
    print("\ntrying to instantiate abstract class")
    obj = Abstract1()
except Exception as e:
    print("     trying to instantiate abstract class Exception : " + str(e))

print("\nInstantiating Impl class")
obj = ImplAbstract1()
obj.display()   #? Overriding display method