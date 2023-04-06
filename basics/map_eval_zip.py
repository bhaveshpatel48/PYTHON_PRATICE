
'''
#~> NOTES
    #% Eval evaluates a string into python expression 
    #% Map function call the function for each item of iterable
    #% Zip does the mapping of each item from both iterable and return object of 'zip'
    
    #% Reference : https://othrif.github.io/python/basics/map.html#:~:text=map%2C%20zip%2C%20eval%2C%20ord%2C%20dir%2C%20pow%20function%201,3%20eval%20%28%29%20...%204%20ord%20%28%29%20
'''

# Eval

print("\n ---------------- EVAl --------------------")
class A:
    
    def __repr__(self) -> str:
        return "Empty Object"

print(eval('A'))    #? It will return python expression A
obj = eval('A')()   #? Eval evaluates a string into python expression
print(obj)  #? calls the __repr__ method
print(eval(' 10 + 15 '))    #? answer would be 25 as integer

# Map - Syntax: map(function, iterable)
print("\n ---------------- Map --------------------")
def square(x):
    return x*x
items = [1,2,3,4]
square_items = map(square,items)    #? Returns a iterable of type 'map'
print(type(square_items))
print(square_items)
print(list(square_items))

print("\n ---------------- Zip --------------------")
l = [1,2,3]
tup = ("first", "second", "third")
zp = zip(l,tup)
print(zp)
print("Type of zp: ",type(zp))
print(list(zp))
