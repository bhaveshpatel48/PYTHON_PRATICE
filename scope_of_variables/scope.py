'''
#% -> Global : Can be used anywhere in program, but before updating this global variable in scope except for global, use 'global var_name'.
#%    Otherwise in another scope it will create varibale with value as global variable

#% -> Local : can be used inside the function, and has scope within that function only
#%    Can't be used inside the inner function of a function

#% -> nonlocal :Varible having scope not local not global
#%    Used generally for inner functions inside function
'''

global_var = 'global'

print("\naccessing global variable in Global Scope: ",global_var)

def localVar():
    global global_var
    
    print("\nAccessing global variable in Local Scope: ",global_var)
    print("     Setting global variable in Local Scope")
    
    global_var = global_var * 2     #~! Here if we don't give 'global global_var' line it won't set the actual global variable value, instead creates its own local variable named 'global_var'
    
    
    local_var = 'local'
    print("\nAccessing local variable in Local Scope: ",local_var)
    
    def localInnerFunction():
        nonlocal local_var          #~* This var has now nonlocal scope 
        
        print("\nAccessing global variable in Inner Function Local Scope: ",global_var)
        
        print("     Accessing local variable in Inner Function Local Scope: ",local_var)
        print("     Setting local variable in Inner Function Local Scope")
        
        local_var = local_var * 2   #~! Here if we don't give 'nonlocal local_var' line it won't set the actual local variable value, instead creates its own local variable named 'local_var'
        print("     Accessing local variable in Inner Function Local Scope, After Updation: ",local_var)
    localInnerFunction()
    
localVar()
