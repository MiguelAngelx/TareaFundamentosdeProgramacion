def inversionMAQC():   
    import math
    n=2018-1961
    P=1500.0
    i=15.0/100.0
    ahorros=P*math.pow(1.0+i,n)
    print ('Valor de P: ' + repr (P))
    print ('Valor de ahorros: ' + repr (ahorros))
    print ('Valor de i: ' + repr (i))
    print ('Valor de n: ' + repr (n))
inversionMAQC()