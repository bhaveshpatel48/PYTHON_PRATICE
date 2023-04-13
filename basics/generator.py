'''
#% -> Funtion having yield statements instead of return statement
#% -> Can have multiple yield statements inside a function
#% -> More pythonic way to create the iterator
#% -> Used for lazy evaluation
        @: Very big file read in chunks
        @: Used for infinite stream of data
        
#% -> References : https://www.pylenin.com/blogs/how-fast-are-generators/
#% -> References : #% -> References : https://www.pylenin.com/blogs/how-fast-are-generators/
    
'''

#? Simple generator function
def generator():
    yield 1
    yield 2
    yield 3

gn = generator()
print("Generator Obj : ",gn)

print(next(gn))

for e in gn:
    print(e)

#? Same like iterator, it won't print anything
for e in gn:
    print(e)
    
#? Generator generates the value on the fly
def countN(n):
    cnt = 0
    while True:
        if cnt<=n:
            cnt+=1
            yield cnt
        else:
            break
print("\nCount Ten Generator")
for i in countN(7):
    print(i)

#? Using class func as generator
class Example:
    def gen(self):
        yield 1
        yield 2

print("\nClass Func as Generator")
ex = Example()
gen = ex.gen()
print(next(gen))
print(next(gen))
print(next(gen))    #? Raise StopIteration error on completion of iteration