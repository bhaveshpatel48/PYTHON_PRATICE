'''
#% -> Mutable default arguments gets initialized once when the function defines
#% -> On everytime we call the function, it's just use that argument value intitialized once.

#% -> Best practices say's never to use the mutable default arguments
'''

def f( l = [] ):     #? here l gets initialized once
    l.append(1)
    print(l)

f()     #? [1]
f()     #? [1,1]
f()     #? [1,1,1]
