def suma (a, b, c=0, d=0):
    if c !=0 and d !=0:
        return a + c + d
    elif c !=0:
        return a + b + c
    else:
        return a + b
    
    print( suma(2+2))