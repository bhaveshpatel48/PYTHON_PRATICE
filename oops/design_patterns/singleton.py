
#% Way-1: Using the __new__ method
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
print("\n Meta Classes")
class SingletonMetaclass(type):
    def __init__(self, *args, **kwargs):
        print("meta class init")
        print("args: ",args)
        print("kwargs: ",kwargs)
        
    def __call__(cls, *args, **kwargs):
        print("cls inside __call__ of meta class: ", cls)
        # if not hasattr(cls, 'instance'):
        #     cls.instance = cls(*args, **kwargs)
        # return cls.instance
        return super().__call__(cls)

print("SingletonMetaclass: ", SingletonMetaclass)
class SingletonWithMetaclass(metaclass=SingletonMetaclass):
    topic = "Singleton object creation in python programming language"
    purpose = "Through out the application, only single instance will exist of this class"
    
    def __new__(cls,*args, **kwargs):
        print("New SingletonMetaclass")
        return super().__new__(cls)
    
    def __init__(self,*args) -> None:
        self.initialized = True
        print("Init SingletonMetaclass")

print("SingletonWithMetaclass.__dict__: , ", SingletonWithMetaclass.__dict__)    

obj = SingletonWithMetaclass()
obj.updated = False
# obj = SingletonWithMetaclass()
print(obj.updated)