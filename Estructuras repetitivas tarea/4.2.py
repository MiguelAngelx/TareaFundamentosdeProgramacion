def montoapagarMAQC():
    sencilla=int(input("ingrese cantidad hamburguesa Sencilla "))
    doble=int(input("ingrese cantidad hamburguesa Doble "))
    triple=int(input("ingrese cantidad hamburguesa Triple "))
    Sencilla=20
    Doble=25 
    Triple=28
    if sencilla  <=0:
        print ("no ahi orden de hamburguesa Sencilla")
    else:
        if sencilla >=1:
            print("el costo de la hamburguesa Sencilla " ,Sencilla*sencilla )

    if doble <=0:
        print("no ahi orden de hamburguesa doble" )
    else:
        if doble >=1:
            print("el costo de la hamburguesa doble es " ,Doble*doble )
    if triple <=0:
        print("no ahi orden de hamburguesa Triples "  )

    else:
        if triple >=1:
            print("el costo es hamburguesa Triples ",Triple*triple )
    pago = Sencilla*sencilla + Doble*doble + Triple*triple 
    tarjeta=pago*0.05
    print("el cargo de la tarjeta es ",tarjeta)
    print("el total a pagar es ",pago + tarjeta)
montoapagarMAQC()