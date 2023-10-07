# Inner function in python are only defined when there parent function is called
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
f()
