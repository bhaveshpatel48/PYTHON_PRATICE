'''
#% -> Iterable is an object which can be iterated over, It has __getitem__ method
#% -> Iterator is an object which has __iter__ and __next__ method
#% -> Every iterator is also an iterable, but not every iterable is an iterator in Python
#% -> Python iter() method works only on iterable objects : It does create iterator from iterable
        It throws an exception TypeError if it is not an iterable
#% -> 

#% -> References : https://www.geeksforgeeks.org/python-difference-iterable-iterator/
#% -> References : https://pyneng.readthedocs.io/en/latest/book/23_oop_special_methods/iterable_iterator.html 
'''

class CountTen:
    def __init__(self,n):
        self.cnt = 0
        self.max_limit = n
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.cnt+=1
        if self.cnt<=self.max_limit:
            return self.cnt
        raise StopIteration()

myRange = CountTen(10)

print("     \nStarting next method call iteration")
print(next(myRange))
print(next(myRange))
print(next(myRange))

print("     \nStarting for loop iteration")
for i in myRange:
    print(i)

#? Only iterate over once - This for loop won't print anything
print("     \nFor loop after iterating iterator completely once")
for i in myRange:
    print(i)
    
print("     \nFor loop iteration of iterator : 1")
for i in CountTen(10):
    print(i)

print("     \nFor loop iteration of iterator : 2")
for i in CountTen(10):  #? Creating new iterator object
    print(i)
    