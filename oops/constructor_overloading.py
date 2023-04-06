
'''
#~> Usage:
    #% -> Factory Methods
    #% -> Constructor Overloading in more pythonic way
    
#~> References:
    #% -> https://www.geeksforgeeks.org/what-is-a-clean-pythonic-way-to-have-multiple-constructors-in-python/ 
'''

class Example(object):
    def __init__(self):
        print("Initializing Example")
        
    @classmethod
    def objWithOneVar(cls,var1):
        obj = cls()
        obj.var1 = var1
        return obj
    
    @classmethod
    def objWithManyVar(cls,*args):
        obj = cls()
        obj.args = args
        return obj
    
    @classmethod
    def objectWithKwargs(cls,**kwargs):
        obj = cls()
        for k,v in kwargs.items():
            setattr(obj,k,v)
        
        obj.display = lambda : print("Display: ",kwargs)
        return obj

print("\nObject with None variable")
ex = Example()

print("\nObject with One variable")
ex = Example.objWithOneVar("foo")
print("Object with one variable: value: ", ex.var1)

print("\nObject with many variables")
ex = Example.objWithManyVar("foo", "bar")
print("Object with many variables, value: ", ex.args)

print("\nObject with many kwargs")
ex = Example.objectWithKwargs(**{'name' : 'Bhavesh', 'surname' : 'vaviya'})
print("Object with many kwargs : ",ex.__dict__)
ex.display()
