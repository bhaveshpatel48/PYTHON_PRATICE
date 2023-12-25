
'''
    #? -> TOPICS Covered
        #^ 1) Dynamic class creation
        #^ 2) Everything is object in python : 100% object oriented programming language
        #^ 4) How metaclass works ?
        #^ 5) Example and usage
        #^ 6) References
'''

#? Every class in python is a instance of a class "type"
from typing import Any


print("\n")
class Lang:
    pass

print(type(Lang.__class__))     #^ <class 'type'>

Lang = type("Lang", (), {})     #^ This is as equivalent as above way of creating the class Lang

#? Classes can be dynamically created at runtime in python
print("\n")
Test = type("Test", (), {"lang" : "Python" , "display": lambda self: print(self.lang)})
obj = Test()
obj.display()

#? Everything is object in python : 100% object oriented programming language
print("\n")
print(type(2))
print(type("Python 3.12"))
def f():
    pass
print(type(f))
print(type([1,2,3]))
print(type((1,2,3)))
print(type({1,2,3}))
print(type({1:2,2:3,3:4}))
print(type(2.30))

print("\n")

#? Meta classes
class MetaClass(type):      #~* meta classes in python extends/inherit the "type" class (Though, it is not mandatory)
    
    def __new__(cls,*args, **kwargs):
        print("Meta Class new method")
        return super().__new__(cls,*args,**kwargs)
    
    def __init__(self,*args, **kwargs):
        print("Meta Class init method")
        
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        print("Meta Class __call__ method")
        
        #~* __call__ of type class internally calls the __new__ method and __init__ method of class having metaclass as this class
        # return super().__call__(*args, **kwargs)
    
        #~* 1) super().__call__(*args, **kwargs)
        #~* 2) self.__init__(self.__new__(self,*args, **kwargs),*args,**kwargs)
        #~# 1 & 2 are equivalent
        
        obj = self.__new__(self,*args, **kwargs)    #? creates a new memory
        self.__init__(obj,*args,**kwargs)   #? initializes that memory
        return obj
    
    def metaDisplay(self):
        print("\nMeta Class Display")
    

#~* In python, object creation and object initialization methods are seperate
class Test(metaclass = MetaClass):
    
    #~* Object creation method
    def __new__(cls, *args, **kwargs):
        print("Test new method")
        
        #~* __new__ always returns, object.__new__ (Parent class of every class in python) creates the object and return the address of that objet
        return super().__new__(cls, *args, **kwargs)
    
    #~* Object initialization method
    def __init__(self) -> None:
        print("Test init method")
        
    @classmethod
    def display(self):
        print("\nTest Display")
        
        
#? Test is now a object of class MetaClass
print("\ntype of Test: ",type(Test))

#? Keeping parenthesis on Test will call the __call__ of it's class "MetaClass" first
#? As "MetaClass" is subclass of "type", it's __call__ is calling type's __call__ method
print("\nMethod in order called while creating the object of Test")
obj = Test()
obj.display()
print("\nTest.__dict__: ", Test.__dict__)
Test.metaDisplay()
print(Test.mro())
Test.version = "3.11"
print(obj.version)
