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
    infq()
print(" globals : ",globals())      
f()
