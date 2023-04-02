class B:
    def __new__(cls):
        print("new of clss B")
        return object.__new__(cls)
    
    def __init__(self):
        print("Id of obj B: ", id(self))
        print("init of class B")
    
print("\n--------B--------------")
print(B())

class C(B):
    def __new__(cls):
        print("new of clss C")
        return super().__new__(cls)
    
    def __init__(self):
        print("Id of obj C: ", id(self))
        super().__init__()
        print("init of class C")
print("\n--------C--------------")
print(C)
print(C())
print("MRO: - ",C.__mro__)

class D:
    #? new always returns
    #? new always takse one argument
    def __new__(cls):
        print("New of class D")
        return super().__new__(cls)
    
    def __init__(self):
        super().__init__()
        print("Init of class D")

class A(D,C):   #~! Extending A(B,C) like this, will give mro consistency error
    def __new__(cls):
        print("New of Class A")
        return C()  #? Within the new, we can return the instance of another class also
    def __init__(self):
        super().__init__()
        print("Init of class A")
        
print("\n--------A--------------")
a = A()
print(a)
print(type(a))
print("MRO:- ",A.__mro__)

class E(D,C):
    def __new__(cls):
        print("New of Class E")
        return super().__new__(cls)
    def __init__(self):
        super().__init__()
        print("Init of class E")
        
print("\n--------E--------------")
e = E()
print(e)

print("MRO:- ",E.__mro__)
