class SingletonClass(object):
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

obj = SingletonClass()
obj.a = 10
obj = SingletonClass()
print(obj.a)