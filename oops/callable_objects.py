'''
#~> Usage:
    #% -> Whenever we want to create a object which can be called just with parentheses, as similar as function call
    #% -> Somehow, till some extent we can acheive that by using the function inside the function
    
    #% -> https://pythoninformer.com/python-language/magic-methods/callable_objects/
'''

class CallableObject(object):
    def __init__(self):
        self.cnt = 0
    
    def __call__(self):
        print("Counter value: ",self.cnt)
        self.cnt += 1
    
print("\nCallable - Class")
increamentCounter = CallableObject()
increamentCounter() #? Print the counter value
increamentCounter() #? Print the counter value

# How same can be acheive through functions inside function
def callableFunc():
    cnt = 0
    def innerFunc():
        nonlocal cnt
        
        print("Counter value: ",cnt)
        cnt += 1
    return innerFunc

print("\nCallable - Function")
funcCallable = callableFunc()
funcCallable() #? Print the counter value
funcCallable() #? Print the counter value

#! Here above function case, if we want to reset the counter - we can't easily do
#! But same can be easily done through callable objects

print("\nCallable - Class - Reset counter")
class CallableObjectResetCounter(object):
    def __init__(self):
        self.cnt = 0
    
    def __call__(self):
        print("Counter value: ",self.cnt)
        self.cnt += 1
    
    def reset(self):
        self.cnt = 0
        
callable = CallableObjectResetCounter()
callable()  #? Print the counter value
callable() #? Print the counter value
callable.reset()
callable()
callable()