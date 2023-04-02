
'''
#~> 1) Magic methods usage :
    #% -> for object representing
    #% -> for callable creating
    #% -> for operator overriding
    #% -> for instance initialization using __init__
    #% -> for instance  creation using __new__
    #% -> for creation of iterable using __iter__ and __next__. Also for __getitem__ overriding
'''


# declare our own string class
class String:

    # magic method to initiate object
    def __init__(self, string):
        self.string = string

    # print our string object
    def __repr__(self):
        return 'Object: {}'.format(self.string)
    
    #~? Operator Overriding
    def __add__(self, other):
        return self.string + other
    
class Integer(object):
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return 'Integer: {}'.format(self.value)
    
    #~? Operator Overriding
    def __add__(self, other):
        print("Plus operator overriding")
        return self.value + other + 10
    
    #~? Operator Overriding
    def __sub__(self, other):
        print("Sub operator overriding")
        return self.value - other-10
    
    #~? Operator Overriding
    def __mul__(self, other):
        print("Mul operator overriding")
        return self.value * other*10

    #~? Operator Overriding
    def __div__(self, other):
        print("Div operator overriding")
        return self.value / other

# Driver Code
if __name__ == '__main__':

    # object creation
    string1 = String('Hello')
    int1 = Integer(10)

    # concatenate String object and a string
    print(string1 +' world')    #~?  here, the + infix operator is oncatinating the String obj and str obj
    
    # Plus
    print(int1 + 20)    #~? This plus (+) will call the __add__ method of Integer object  
    
    # Sub
    print(int1 - 20)    #~? This sub (-) will call the __sub__ method of Integer object
    
    # Mul
    print(int1 * 20)    #~? This mul (*) will call the __mul__ method of Integer object
    
    # Div
    # print(int1//20)
    