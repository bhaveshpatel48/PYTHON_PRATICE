
'''
#~> Why we use __name__ special variable ?
    #% -> __name__ is a built-in variable which evaluates to the name of the current module
    #% -> If this file is being imported from another module, __name__ will be set to the module’s name
'''

import File1 

print ("File2 __name__ = %s" %__name__) 

if __name__ == "__main__": 
    print ("File2 is being run directly")
else: 
    print ("File2 is being imported")