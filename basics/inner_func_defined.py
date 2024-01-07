import dis

# Inner function in python are only defined when there parent function is called

#~? Syntax error comes because the entire code is parsed before the compilation, this to detect the syntax error as early as possible
#~? Inner function infq, infg and idhn are only compiled when there outer function is called, lazy compilation
def f():
    a = 10
    def infq():
        b = 20
        def infg():
            c = 30
            def idhn():
                pass
            print(" locals : ",locals())
        print(" locals : ",locals())
        infg()
    print(" locals : ",locals())
    
    #? The proof that the nested inner function (infg & inhn) is not yet compiled and saved to locals of f
    print(" locals : ",locals().get('infq').__dict__)
    
    infq()
print(" globals : ",globals())   
print("F has __code__: ",hasattr(f, '__code__'))  #~^ When the function is compiled, its bytecodes is stored in __code__ attribute of function object 
print(dis.dis(f))
f()
