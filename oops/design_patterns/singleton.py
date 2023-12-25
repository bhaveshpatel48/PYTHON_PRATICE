
#% Way-1: Using the __new__ method
#~? Needed to override __new__ in every class that needs to be singleton 
class SingletonClass(object):
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

obj = SingletonClass()
obj.a = 10
obj = SingletonClass()
print(obj.a)

#% Way-2: using decorator
#~? The decorator can be used on any class that needs to be singleton, DRY code practice
def singleton(cls):
    
    def get_instance(*args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = cls(*args, **kwargs)
        return cls.instance
    return get_instance
@singleton
class SingletonWithDecorator(object):
    pass

obj = SingletonWithDecorator()
obj.updated = False
obj = SingletonWithDecorator()
print(obj.updated)


#% Way3: using metacclass
#~? Most advanced way to create a singleton class instance
#~? DRY Practice
#~? Provide metaclass= attribute to every class defination that needs to be singleton
class SingletonMetaclass(type):
    def __init__(self, *args, **kwargs):
        print("meta class init")
        print("args: ",args)
        print("kwargs: ",kwargs)
        
    def __call__(self, *args, **kwargs):
        print("cls inside __call__ of meta class: ", self)
        if not hasattr(self, 'instance'):
            self.instance = super().__call__(self, *args, **kwargs)
        return self.instance

class SingletonWithMetaclass(metaclass=SingletonMetaclass):
    topic = "Singleton object creation in python programming language"
    purpose = "Through out the application, only single instance will exist of this class"
    
    def __new__(cls,*args, **kwargs):
        print("New SingletonMetaclass")
        return super().__new__(cls)
    
    def __init__(self,*args) -> None:
        self.initialized = True
        print("Init SingletonMetaclass")    

obj = SingletonWithMetaclass()
obj.updated = False

print(obj.updated)

obj.name = "john"

obj = SingletonWithMetaclass()
print(obj.name)