'''
#% -> Iterable is an object which can be iterated over, It has __getitem__ method
#% -> Iterator is an object which has __iter__ and __next__ method
#% -> Every iterator is also an iterable, but not every iterable is an iterator in Python
#% -> Python iter() method works only on iterable objects : It does create iterator from iterable
        It throws an exception TypeError if it is not an iterable
#% -> Iterator can be iterated only once

#% -> References : https://www.geeksforgeeks.org/python-difference-iterable-iterator/
#% -> References : https://pyneng.readthedocs.io/en/latest/book/23_oop_special_methods/iterable_iterator.html 
'''

''' ----------------------  Check obj is iterable or not ------------------------'''
# Function to check object is iterable or not
def it(ob):
    try:
        iter(ob)
        return True
    except TypeError:
        return False

# Driver Code
print("\n Check if python object is an iterable")
for i in [34, [4, 5], (4, 5),{"a":4}, "dfsdf", 4.5]:
    print("     ",i,"is iterable :",it(i))


''' ----------------------  Create Iterable Object ------------------------'''
class Iterable(object):
    def __init__(self):
        self.items={}
    
    def __setitem__(self,key,value):
        self.items[key]=value
    
    def __getitem__(self,key):
        return self.items.get(key,None)
    
class Items:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        print('     Iterable __getitem__')
        return self.items[index]

print("\n Creating Iterable Object")
iterable = Iterable()
iterable["name"] = "Bhavesh Vaviya"
print("     ",iterable['name'])

iterable_2 = Items([1,2,3,4,5])
print("     ",iterable_2[3])


''' ----------------------  Converting Iterable to Iterator ------------------------'''
name = "Bhavesh Vaviya"
iteratorObj = iter(name)
print("\n Converting Iterable to Iterator")
print("     ",next(iteratorObj))
print("     ",next(iteratorObj))
print("     ",next(iteratorObj))    #? Once the iteration is over, on calling next will raise StopIteration exception